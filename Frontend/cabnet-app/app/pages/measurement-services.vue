<template>
<div class="h-[1000px]"></div>


  <div class="box w-full h-[100vh] rounded-lg relative" style="background-color: #f3f4f6;" ref="boxRef">
    <div>
    <h1 class="absolute title1 text-4xl font-bold text-center pt-40 opacity-0">Scroll down to see the animation1</h1>
    <h1 class="absolute title2 text-4xl font-bold text-center pt-40 opacity-0">Scroll down to see the animation2</h1>
    <h1 class="absolute title3 text-4xl font-bold text-center pt-40 opacity-0">Scroll down to see the animation3</h1>
    </div>
  </div>


<div class="h-[1000px]"></div>
</template>


<script setup lang="ts">
import {gsap} from "gsap";
import {onMounted, ref, onUnmounted} from "vue";
import { ScrollTrigger } from "gsap/all";

gsap.registerPlugin(ScrollTrigger);

const boxRef = ref<HTMLElement | null>(null);
const ctx = ref<gsap.Context | null>(null);

onMounted(() => {

  ctx.value = gsap.context(() => {


  const tl = gsap.timeline({
    scrollTrigger:{
      trigger: boxRef.value,
      start: 'top top',
      end: '+=3000px top',
      pin: true,
      scrub: true,
      markers: true
    }
  });

  tl.to('.title1', {
    color: '#00ff00',
    duration: 10,
    opacity: 1,
    y: -50
  })


 tl.to('.title2', {
    color: '#00ff00',
    duration: 10,
    opacity: 1,
    y: -50
  })
    .to('.title1', { opacity: 0, duration: 5 }, "<") // fade out after a delay of 1 second

 tl.to('.title3', {
    color: '#00ff00',
    duration: 10,
    opacity: 1,
    y: -50
  })
    .to('.title2', { opacity: 0, duration: 5 }, "<") // fade out after a delay of 1 second

  tl.to(".box", {
    backgroundColor: '#0000ff',
    duration: 30,
  }, 0)

})
})

onUnmounted(() => {
  ctx.value?.revert()
})

</script>
