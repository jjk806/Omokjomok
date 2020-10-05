<template>
  <div>
    <h1>묘 수 풀 이</h1>
    <div class="d-flex align-items-center justify-content-center" id="trick" style="height:75vh; text-align:center;">
      <div>
        <b-button @click='testSetBoard1' variant="white" router :to="{ name: 'trickSolving_bigBoard' }" class="btn ml-3 mb-5" type="submit"><img class="btn-img" src="../../assets/one_black.png" width="100"></b-button>
        <b-button @click='testSetBoard2' variant="white" router :to="{ name: 'trickSolving_bigBoard' }" class="btn ml-3 mb-5" type="submit"><img class="btn-img" src="../../assets/two_black.png" width="100"></b-button>
        <b-button @click='testSetBoard3' variant="white" router :to="{ name: 'trickSolving_bigBoard' }" class="btn ml-3 mb-5" type="submit"><img class="btn-img" src="../../assets/three.png" width="100"></b-button>
        <b-button @click='testSetBoard4' variant="white" router :to="{ name: 'trickSolving_bigBoard' }" class="btn ml-3 mb-5" type="submit"><img class="btn-img" src="../../assets/four.png" width="100"></b-button>
        <b-button @click='testSetBoard5' variant="white" router :to="{ name: 'trickSolving_bigBoard' }" class="btn ml-3 mb-5" type="submit"><img class="btn-img" src="../../assets/five.png" width="100"></b-button>
        <br>
        <button @click="check()" class="btn ml-3 mt-3" type="submit"><img class="btn-img" src="../../assets/six.png" width="100"></button>
        <button @click="check()" class="btn ml-3 mt-3" type="submit"><img class="btn-img" src="../../assets/seven.png" width="100"></button>
        <button @click="check()" class="btn ml-3 mt-3" type="submit"><img class="btn-img" src="../../assets/eight.png" width="100"></button>
        <button @click="check()" class="btn ml-3 mt-3" type="submit"><img class="btn-img" src="../../assets/nine.png" width="100"></button>
        <button @click="check()" class="btn ml-3 mt-3" type="submit"><img class="btn-img" src="../../assets/ten.png" width="100"></button>
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
    ...mapActions(['testSetBoard1', 'testSetBoard2', 'testSetBoard3', 'testSetBoard4', 'testSetBoard5']),
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
