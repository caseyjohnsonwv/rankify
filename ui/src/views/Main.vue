<template>
  <div class="Main">
    <h1>This is the Rankify UI itself!</h1>
    <button v-on:click="test">Test Auth</button>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'Main',
  methods: {
    test: async function() {
      let token = JSON.parse(this.$cookie.get('spotify_token'));
      let query = 'Mac Miller Swimming';
      let type = 'album';
      const path = encodeURI(`${process.env.VUE_APP_API_URL}/spotify/import?type=${type}&query=${query}`);
      await axios.post(path, {token}).then((res) => {
        console.log(res);
      });
    }
  },
  created() {
    const token = this.$cookie.get('spotify_token')
    if (token === null) {
      this.$router.push({name: 'Landing'});
    }
  }
}
</script>
