<template>
  <b-container fluid>
    <b-row class="mt-2">
      <b-col offset=2 cols=4>
        <b-button variant="dark" block v-b-modal.modal-create-room>
          AI 대전
          <img src="../../assets/ai.jpg" alt="" class="my-2">
        </b-button>
      </b-col>
      <b-col cols=4>
        <b-button variant="dark" block router :to="{ name: 'TrickSolve' }">
          묘수 풀이
          <img src="../../assets/myosu.png" alt="" class="my-2">
          </b-button>
      </b-col>
      <b-col cols=2>
        <MyInfo />
      </b-col>
    </b-row>
    <b-row class="mt-5">
      <b-col offset=2 cols=4>
        <b-button block>AI 대전 설명
          <AiCarousel  class="my-2"/>
        </b-button>
      </b-col>
      <b-col cols=4>
        <b-button block>묘수 풀이 설명
          <AiCarousel  class="my-2"/>
        </b-button>
      </b-col>
      <b-col cols=2>
        <Rating />
      </b-col>
    </b-row>

  <!--  -->
  <CreateRoom />


  </b-container>
</template>

<script>
import AiCarousel from "../../components/common/AiCarousel.vue";
import Rating from "../../components/common/Rating.vue";
import MyInfo from "../../components/common/MyInfo.vue";
import CreateRoom from "../../components/common/CreateRoom.vue";
// import axios from "axios";

export default {
  name: "Mainpage",
  components: {
    AiCarousel,
    Rating,
    MyInfo,
    CreateRoom,
  },
  watch: {},
  methods: {
  },
  data: () => {
    return {};
  },
};
</script>


<style scoped>
.wrapB {
  width: 1200px;
}

img {
  width: 460px;
  height: 210px !important;
}

</style>