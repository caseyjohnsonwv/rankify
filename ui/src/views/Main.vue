<template>
  <div class="Main">
    <h1>This is the Rankify UI itself!</h1>
    <button v-on:click="test">Load Test Data</button>
    <div class="container">
      <div class="row">
        <div class="col">
          <h3>Unranked Songs</h3>
          <draggable v-model="unranked_songs" group="songs" @start="drag=true" @end="drag=false">
            <Song v-for="song in unranked_songs"
              :key="song.uri"
              :name="song.name"
              :artist="song.artist"
              :album_cover="song.album_cover"
              :preview_url="song.preview_url"
              :uri="song.uri"
            ></Song>
          </draggable>
        </div>
        <div class="col">
          <h3>Ranked Songs</h3>
          <draggable v-model="ranked_songs" group="songs" @start="drag=true" @end="drag=true">
            <Song v-for="song in ranked_songs"
              :key="song.uri"
              :name="song.name"
              :artist="song.artist"
              :album_cover="song.album_cover"
              :preview_url="song.preview_url"
              :uri="song.uri"
            ></Song>
          </draggable>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import draggable from 'vuedraggable'
import Song from '@/components/Song.vue'

export default {
  name: 'Main',
  components: {
    draggable,
    Song,
  },
  data() {
    return {
      all_songs: new Set(),
      unranked_songs: [],
      ranked_songs: [],
    };
  },
  methods: {
    test: async function() {
      let token = JSON.parse(this.$cookie.get('spotify_token'));
      let query = 'Mac Miller Swimming';
      let type = 'album';
      const path = encodeURI(`${process.env.VUE_APP_API_URL}/spotify/import?type=${type}&query=${query}`);
      await axios.post(path, {token})
      .then((res) => {
        console.log(res);
        res.data.tracks.forEach((track) => {
          if (!this.all_songs.has(track.uri)) {
            this.all_songs.add(track.uri);
            this.unranked_songs.push({
              'uri':track.uri,
              'name':track.name,
              'artist':res.data.artist,
              'preview_url':track.preview_url,
              'album_cover':res.data.image_url,
            });
          }
        });
      })
      .catch((err) => {
        console.error(err.toJSON());
        if (err.response.status == 401) {
          alert("Session has expired, please log in again!")
          this.$router.push({name: 'Landing'});
        }
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
