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
      let query = 'Mac Miller';
      const path = encodeURI(`${process.env.VUE_APP_API_URL}/spotify/search?query=${query}`);
      await axios.post(path, {token}).then((res) => {
        console.log(res);
        var names = []
        res.data.results[0].items.forEach(item => names.push(item.name));
        alert(names);
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
