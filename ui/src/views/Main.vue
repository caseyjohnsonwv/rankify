<template>
  <div class="Main">
    <h1>This is the Rankify UI itself!</h1>
  </div>
</template>

<script>
export default {
  name: 'Main',
  methods: {

  },
  created() {
    const token = this.$cookie.get('spotify_token')
    if (token === null) {
      this.$router.push({name: 'Landing'});
    }
  }
}
</script>
