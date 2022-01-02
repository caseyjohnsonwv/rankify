<template>
  <div class="container song-wrapper card-body shadow"
    :class="{'playing':active}">
    <div class="row">
      <div class="col-2">
        <img class="img-thumbnail img-fluid" :src="album_cover">
      </div>
      <div class="col-10 song-data-wrapper">
        <div class="col-9">
          <h5 class="no-margin-bottom">{{name}}</h5>
        </div>
        <div class="col-3">
          <p class="no-margin-bottom">{{artist}}</p>
          <p class="no-margin-bottom">{{album_name}}</p>
        </div>
      </div>
    </div>
  </div>
</template>

<style>
.song-wrapper {
  margin-bottom: 5px;
  border: 1px solid #bbb;
}
.song-data-wrapper {
  display: flex;
  justify-content: center;
  align-items: center;
}
.no-margin-bottom {
  margin-bottom: 0;
}
.playing {
  background: rgba(0, 0, 0, 0.1);
}
</style>

<script>
export default {
  name: 'Song',
  props: [
    'name',
    'artist',
    'preview_url',
    'album_cover',
    'album_name',
    'uri',
  ],
  data() {
    return {
      active: false
    }
  },
};
</script>
