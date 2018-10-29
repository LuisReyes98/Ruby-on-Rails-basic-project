<template >
	 <Slide>
      <a id="login" href="#">
        <span>Iniciar Sesión</span>
      </a>    
      <a id="home"  href="/home"> 
        
        <span>
          <i class="mi home"></i>
          Inicio
        </span>  
      </a>
      <a id="themes" href="/themes">
        <span>Temas</span>
      </a>
      <a id="critics" href="/critics">
        <span>Criticas</span>
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