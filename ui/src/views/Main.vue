<template>
  <div class="Main">
    <h1>This is the Rankify UI itself!</h1>
    <button v-on:click="test">Load Test Data</button>
    <div class="container">
      <div class="row">
        <div class="col">
          <h3>Unranked Songs</h3>
          <draggable v-model="unranked_songs" group="songs">
            <Song :ref="song.preview_url"
            v-for="song in unranked_songs"
              :key="song.uri"
              :name="song.name"
              :artist="song.artist"
              :album_cover="song.album_cover"
              :album_name="song.album_name"
              :preview_url="song.preview_url"
              :uri="song.uri"
            v-on:click.native="play_preview(song.preview_url);"
            ></Song>
          </draggable>
        </div>
        <div class="col">
          <h3>Ranked Songs</h3>
          <draggable v-model="ranked_songs" group="songs">
            <Song :ref="song.preview_url"
            v-for="song in ranked_songs"
              :key="song.uri"
              :name="song.name"
              :artist="song.artist"
              :album_cover="song.album_cover"
              :album_name="song.album_name"
              :preview_url="song.preview_url"
              :uri="song.uri"
            v-on:click.native="play_preview(song.preview_url)"
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
      now_playing: null,
    };
  },
  methods: {
    play_preview: function(preview_url) {
      // find old and new songs to toggle playing
      if (this.now_playing === null) {
        // first time playback
        this.now_playing = new Audio(preview_url);
        this.now_playing.play();
        this.$refs[this.now_playing.src][0].active = true;
      } else {
        if (this.now_playing.src === preview_url) {
          if (this.now_playing.paused || this.now_playing.ended) {
            // resume or replay
            this.now_playing.play();
            this.$refs[this.now_playing.src][0].active = true;
          } else {
            // pause
            this.now_playing.pause();
            this.$refs[this.now_playing.src][0].active = false;
          }
        }
        else {
          // song change
          this.$refs[this.now_playing.src][0].active = false;
          this.now_playing.pause();
          this.now_playing = new Audio(preview_url);
          this.now_playing.play();
          this.$refs[this.now_playing.src][0].active = true;
        }
      }
    },
    test: async function() {
      let token = JSON.parse(this.$cookie.get('spotify_token'));
      let query = 'Tyler Childers';
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
              'album_name':res.data.album,
            });
          }
        });
      })
      .catch((err) => {
        console.error(err.toJSON());
        if (err.response.status == 401) {
          alert("Session has expired, please log in again!")
          this.$cookie.delete('spotify_token');
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
