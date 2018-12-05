
import Vue from 'vue/dist/vue.esm';
import Slide from '../components/slide.vue';

document.addEventListener('DOMContentLoaded', () => {
  
  const slide = new Vue({
    el: 'slide',
    template: '<Slide/>',
    components: { Slide }
  });

 
	
});