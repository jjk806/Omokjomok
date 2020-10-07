<template>
  <div>
    <h1>무적수 화월</h1>
    <div class="d-flex align-items-center justify-content-center" id="trick" style="height:75vh; text-align:center;">
      <div>
        <b-button @click='whaWallSetBoard1' variant="white" router :to="{ name: 'trickSolving_bigBoard' }" class="btn ml-3 mb-5" type="submit"><img class="btn-img" src="../../assets/one_black.png" width="100"></b-button>
        <b-button @click='whaWallSetBoard2' variant="white" router :to="{ name: 'trickSolving_bigBoard' }" class="btn ml-3 mb-5" type="submit"><img class="btn-img" src="../../assets/two_black.png" width="100"></b-button>
        <b-button @click='whaWallSetBoard3' variant="white" router :to="{ name: 'trickSolving_bigBoard' }" class="btn ml-3 mb-5" type="submit"><img class="btn-img" src="../../assets/three.png" width="100"></b-button>
        <b-button @click='whaWallSetBoard4' variant="white" router :to="{ name: 'trickSolving_bigBoard' }" class="btn ml-3 mb-5" type="submit"><img class="btn-img" src="../../assets/four.png" width="100"></b-button>
        <b-button @click='whaWallSetBoard5' variant="white" router :to="{ name: 'trickSolving_bigBoard' }" class="btn ml-3 mb-5" type="submit"><img class="btn-img" src="../../assets/five.png" width="100"></b-button>
      </div>
    </div>
  </div>
</template>

<script>
import { mapActions } from "vuex";

export default {
  name: "TrickSolve",
  methods: {
    check() {
      alert('추후 업데이트 예정')
    },
    ...mapActions(['whaWallSetBoard1', 'whaWallSetBoard2', 'whaWallSetBoard3', 'whaWallSetBoard4', 'whaWallSetBoard5']),
  },
  created() {
    this.clearMatch();
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
