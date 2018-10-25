class Frontend::CriticsController < ApplicationController
  before_action :set_frontend_critic, only: [:show, :edit, :update, :destroy]

  # GET /frontend/critics
  # GET /frontend/critics.json
  def index
    @frontend_critics = Frontend::Critic.all
  end

  # GET /frontend/critics/1
  # GET /frontend/critics/1.json
  def show
  end

  # GET /frontend/critics/new
  def new
    @frontend_critic = Frontend::Critic.new
  end

  # GET /frontend/critics/1/edit
  def edit
  end

  # POST /frontend/critics
  # POST /frontend/critics.json
  def create
    @frontend_critic = Frontend::Critic.new(frontend_critic_params)

    respond_to do |format|
      if @frontend_critic.save
        format.html { redirect_to @frontend_critic, notice: 'Critic was successfully created.' }
        format.json { render :show, status: :created, location: @frontend_critic }
      else
        format.html { render :new }
        format.json { render json: @frontend_critic.errors, status: :unprocessable_entity }
      end
    end
  end

  # PATCH/PUT /frontend/critics/1
  # PATCH/PUT /frontend/critics/1.json
  def update
    respond_to do |format|
      if @frontend_critic.update(frontend_critic_params)
        format.html { redirect_to @frontend_critic, notice: 'Critic was successfully updated.' }
        format.json { render :show, status: :ok, location: @frontend_critic }
      else
        format.html { render :edit }
        format.json { render json: @frontend_critic.errors, status: :unprocessable_entity }
      end
    end
  end

  # DELETE /frontend/critics/1
  # DELETE /frontend/critics/1.json
  def destroy
    @frontend_critic.destroy
    respond_to do |format|
      format.html { redirect_to frontend_critics_url, notice: 'Critic was successfully destroyed.' }
      format.json { head :no_content }
    end
  end

  private
    # Use callbacks to share common setup or constraints between actions.
    def set_frontend_critic
      @frontend_critic = Frontend::Critic.find(params[:id])
    end

    # Never trust parameters from the scary internet, only allow the white list through.
    def frontend_critic_params
      params.require(:frontend_critic).permit(:score, :title, :description, :theme_id)
    end
end
