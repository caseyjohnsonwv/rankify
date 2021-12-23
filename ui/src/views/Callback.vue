<template>
  <div class="Callback">
    <p>Redirecting...</p>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'Callback',
  methods: {
    completeOAuth: async function() {
      const state = this.$route.query.state;
      const code = this.$route.query.code;
      const session_state = this.$session.get('state')
      if (state === null || code === null || state !== session_state) {
        this.$router.push({name: 'Landing'});
      }
      else {
        const path = `${process.env.VUE_APP_API_URL}/auth/callback?state=${state}&code=${code}`
        // use get request because get is cheaper than post on s3
        await axios.get(path).then((res) => {
          this.$cookie.set('spotify_token', res.data.token);
        });
        this.$router.push({name: 'Main'});
      }
    }
  },
  created() {
    this.completeOAuth();
  }
}
</script>
