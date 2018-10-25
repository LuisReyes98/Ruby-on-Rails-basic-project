class Frontend::ThemesController < ApplicationController
  before_action :set_frontend_theme, only: [:show, :edit, :update, :destroy]

  # GET /frontend/themes
  # GET /frontend/themes.json
  def index
    @frontend_themes = Frontend::Theme.all
  end

  # GET /frontend/themes/1
  # GET /frontend/themes/1.json
  def show
  end

  # GET /frontend/themes/new
  def new
    @frontend_theme = Frontend::Theme.new
  end

  # GET /frontend/themes/1/edit
  def edit
  end

  # POST /frontend/themes
  # POST /frontend/themes.json
  def create
    @frontend_theme = Frontend::Theme.new(frontend_theme_params)

    respond_to do |format|
      if @frontend_theme.save
        format.html { redirect_to @frontend_theme, notice: 'Theme was successfully created.' }
        format.json { render :show, status: :created, location: @frontend_theme }
      else
        format.html { render :new }
        format.json { render json: @frontend_theme.errors, status: :unprocessable_entity }
      end
    end
  end

  # PATCH/PUT /frontend/themes/1
  # PATCH/PUT /frontend/themes/1.json
  def update
    respond_to do |format|
      if @frontend_theme.update(frontend_theme_params)
        format.html { redirect_to @frontend_theme, notice: 'Theme was successfully updated.' }
        format.json { render :show, status: :ok, location: @frontend_theme }
      else
        format.html { render :edit }
        format.json { render json: @frontend_theme.errors, status: :unprocessable_entity }
      end
    end
  end

  # DELETE /frontend/themes/1
  # DELETE /frontend/themes/1.json
  def destroy
    @frontend_theme.destroy
    respond_to do |format|
      format.html { redirect_to frontend_themes_url, notice: 'Theme was successfully destroyed.' }
      format.json { head :no_content }
    end
  end

  private
    # Use callbacks to share common setup or constraints between actions.
    def set_frontend_theme
      @frontend_theme = Frontend::Theme.find(params[:id])
    end

    # Never trust parameters from the scary internet, only allow the white list through.
    def frontend_theme_params
      params.require(:frontend_theme).permit(:name, :description)
    end
end
