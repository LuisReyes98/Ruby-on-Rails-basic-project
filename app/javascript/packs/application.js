
import Vue from 'vue/dist/vue.esm';
import Slide from '../components/slide.vue';
//import Test from '../components/test.vue';
//import Nav from '../components/nav.vue';

document.addEventListener('DOMContentLoaded', () => {
  
  const slide = new Vue({
    el: 'slide',
    data:{
			login: "Iniciar Sesión"
    },
    template: '<Slide message="login"/>',
    components: { Slide }
  });

 
	
});