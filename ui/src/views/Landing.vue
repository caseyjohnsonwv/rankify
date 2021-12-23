<template>
  <div class="Landing">
    <h1>This is the landing page!</h1>
    <button v-on:click="initiateOAuth">Login with Spotify</button>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'Landing',
  methods: {
    initiateOAuth: function() {
        const path = `${process.env.VUE_APP_API_URL}/auth`
        axios.get(path).then((res) => {
          this.$session.set('state', res.data.state)
          window.location.href = res.data.spotify_url
        });
    }
  }
}
</script>
