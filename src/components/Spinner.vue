<template>
  <!-- Loading animation container -->
  <div class="loading">
   <img src="../../assets/meta/loading.svg"/>
 </div>
</template>

<script>

export default {
  name: 'Spinner'
}
</script>
<style>
.loading img {
  max-width: 100%;
  margin-top: 50%
}
.loading {
  top: 0;
  position: fixed;
  width: 100%;
  height: 100%;
  background: rgba(255, 255, 255, .9);
  z-index: 100
}
</style>
