<template>
  <div class="Callback">
    <AuthHandler msg="This is the Spotify callback handler!"/>
  </div>
</template>

<script>
// @ is an alias to /src
import AuthHandler from '@/components/AuthHandler.vue'

export default {
  name: 'Callback',
  components: {
    AuthHandler
  }
}
</script>
