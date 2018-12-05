<template >
	 <Slide class="" id="slide_nav_bar">
      <a id="login" href="#" data-toggle="modal" data-target="#login-modal" >
        <span>
        <i class="mdi mdi-account-outline"></i>
        Iniciar Sesión</span>
      </a>    
      <a id="home"  href="/">         
        <span>
          <i class="mdi mdi-home"></i>
          Inicio
        </span>  
      </a>
      <a id="themes" href="/themes">
        <span>
        <i class="mdi mdi-bookmark"></i>
        Temas
        </span>
      </a>
      <a id="critics" href="/critics">
        <span>
        <i class="mdi mdi-star-circle"></i>
        Criticas
        </span>
      </a>
    </Slide>
<!-- .mdi.mdi-view-dashboard -->

</template>
<script>
	import { Slide } from 'vue-burger-menu'  // import the CSS transitions you wish to use, in this case we are using `Slide`

	export default {
	    components: {
	        Slide // Register your component
	    }
	}
</script>

<style scoped>
  .bm-burger-button {
    position: -webkit-sticky; /* Safari */
    position: sticky;    
  }
</style>