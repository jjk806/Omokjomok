<template>
  <b-container fluid>
    <b-row class="mt-5">
      <b-col offset=2 cols=4>
        <b-button block v-b-modal.modal-create-room>AI 대전
          <img src="../../assets/ai.jpg" alt="">
        </b-button>
      </b-col>
      <b-col cols=4>
        <b-button block>묘수 풀이
          <img src="../../assets/kakao.jpg" alt="">
          </b-button>
      </b-col>
      <b-col cols=2>
        <MyInfo />
      </b-col>
    </b-row>
    <b-row class="mt-5">
      <b-col offset=2 cols=4>
        <b-button block>ai carousel
          <AiCarousel />
        </b-button>
      </b-col>
      <b-col cols=4>
        <b-button block>myosu carousel
          <AiCarousel />
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

export default {
  name: "Mainpage",
  components: {
    AiCarousel,
    Rating,
    MyInfo,
    CreateRoom,
  },
  watch: {},
  created() {},
  methods: {
    clickCrateRoom() {},
    resetModal() {},
    handleOk() {},
  },
  data: () => {
    return {};
  },
};
</script>


<style>
.wrapB {
  width: 1200px;
}

</style>