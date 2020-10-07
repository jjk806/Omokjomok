<template>
  <div>
    <h1>무적수 포월</h1>
    <div class="d-flex align-items-center justify-content-center" id="trick" style="height:75vh; text-align:center;">
      <div>
        <b-button v-if="tricklist[5]" @click='poWallSetBoard1' variant="white" router :to="{ name: 'trickSolving_bigBoard' }" class="btn ml-3 mb-5" type="submit"><img class="btn-img" src="../../assets/one_black.png" width="100"></b-button>
        <b-button v-else @click='poWallSetBoard1' variant="white" router :to="{ name: 'trickSolving_bigBoard' }" class="btn ml-3 mb-5" type="submit"><img class="btn-img" src="../../assets/one.png" width="100"></b-button>

        <b-button v-if="tricklist[6]" @click='poWallSetBoard1' variant="white" router :to="{ name: 'trickSolving_bigBoard' }" class="btn ml-3 mb-5" type="submit"><img class="btn-img" src="../../assets/two_black.png" width="100"></b-button>
        <b-button v-else @click='poWallSetBoard2' variant="white" router :to="{ name: 'trickSolving_bigBoard' }" class="btn ml-3 mb-5" type="submit"><img class="btn-img" src="../../assets/two.png" width="100"></b-button>

        <b-button v-if="tricklist[7]" @click='poWallSetBoard1' variant="white" router :to="{ name: 'trickSolving_bigBoard' }" class="btn ml-3 mb-5" type="submit"><img class="btn-img" src="../../assets/three.png" width="100"></b-button>
        <b-button v-else @click='poWallSetBoard3' variant="white" router :to="{ name: 'trickSolving_bigBoard' }" class="btn ml-3 mb-5" type="submit"><img class="btn-img" src="../../assets/three.png" width="100"></b-button>

        <b-button v-if="tricklist[8]" @click='poWallSetBoard1' variant="white" router :to="{ name: 'trickSolving_bigBoard' }" class="btn ml-3 mb-5" type="submit"><img class="btn-img" src="../../assets/four_black.png" width="100"></b-button>
        <b-button v-else @click='poWallSetBoard4' variant="white" router :to="{ name: 'trickSolving_bigBoard' }" class="btn ml-3 mb-5" type="submit"><img class="btn-img" src="../../assets/four.png" width="100"></b-button>

        <b-button v-if="tricklist[9]" @click='poWallSetBoard1' variant="white" router :to="{ name: 'trickSolving_bigBoard' }" class="btn ml-3 mb-5" type="submit"><img class="btn-img" src="../../assets/five_black.png" width="100"></b-button>
        <b-button v-else @click='poWallSetBoard5' variant="white" router :to="{ name: 'trickSolving_bigBoard' }" class="btn ml-3 mb-5" type="submit"><img class="btn-img" src="../../assets/five.png" width="100"></b-button>
      </div>
    </div>
  </div>
</template>

<script>
import { mapActions } from "vuex";

import http from "../../util/http-common"
export default {
  name: "TrickSolve",
  data: () => {
    return {
      tricklist: []
    };
  },
  methods: {
    check() {
      alert('추후 업데이트 예정')
    },
    ...mapActions(['poWallSetBoard1', 'poWallSetBoard2', 'poWallSetBoard3', 'poWallSetBoard4', 'poWallSetBoard5','initSetBoard',"clearMatch"]),
  },
  created() {
    this.clearMatch();
    const config = {
      headers: {
        Authorization: `Token ${this.$cookies.get('auth-token')}`
      }
    }
    // pk 값 가져오는 요청
    http.get("rest_auth/user/", config)
    .then(res => {
      
      // tricklist 가져오는 요청
      http.post("omok_game/tricklist/", { "pk": res.data.pk })
      .then(re => {
        console.log('tricklist', re.data)
        this.tricklist = re.data
      })
      .catch(err => {
        console.log(err)
      })
    })
    .catch(err => {
      console.log(err)
    })
  },
}
</script>

<style scoped>

#trick {
  background-image: url('../../assets/omok_pan2.png');
  background-repeat: no-repeat;
  background-position: center center;
  background-size: cover;
  width: 100%;
}

img {
  width: 100px;
  height: 100px !important;
}
</style>
