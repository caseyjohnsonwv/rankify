<template>
  <div>
    <p>Name: {{name}}</p>
  </div>
</template>

<script>
export default {
  name: 'Song',
  props: [
    'name',
    'artist',
    'preview_url',
    'album_cover',
    'uri'
  ],
};
</script>
