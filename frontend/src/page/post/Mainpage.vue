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
        
        <!-- <MyInfo /> -->
        <b-container class="my-5">
          <b-row>
            <b-col class="text-left">
              <h4>SSAFY1 정보</h4>
            </b-col>
          </b-row>
          <b-row>
            <b-col class="text-left">승률</b-col>
            <b-col class="text-left">{{ userInfo.rate}} %</b-col>
          </b-row>
          <b-row>
            <b-col class="text-left">묘수풀이</b-col>
            <b-col class="text-left">{{ userInfo.score}} 점</b-col>
          </b-row>
          <b-row>
            <b-col class="text-left">기보</b-col>
            <b-col class="text-left"><a href="">보러가기</a></b-col>
          </b-row>
        </b-container>
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
        <!-- <Rating /> -->
        <b-row>
          <b-col class="text-left">
            <h4>실시간 순위</h4>
          </b-col>
        </b-row>
        <b-row class="my-2">
          <b-col cols="3" class="text-left">No.</b-col>
          <b-col cols="9" class="text-left">Name</b-col>
        </b-row>
        <b-row>
          <b-col cols="3" class="text-left">1</b-col>
          <b-col cols="9" class="text-left">{{ userrank[0] }}</b-col>
        </b-row>
        <b-row>
          <b-col cols="3" class="text-left">2</b-col>
          <b-col cols="9" class="text-left">{{ userrank[1] }}</b-col>
        </b-row>
        <b-row>
          <b-col cols="3" class="text-left">3</b-col>
          <b-col cols="9" class="text-left">{{ userrank[2] }}</b-col>
        </b-row>
        <b-row>
          <b-col cols="3" class="text-left">4</b-col>
          <b-col cols="9" class="text-left">{{ userrank[3] }}</b-col>
        </b-row>
        <b-row>
          <b-col cols="3" class="text-left">5</b-col>
          <b-col cols="9" class="text-left">{{ userrank[4] }}</b-col>
        </b-row>
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

import http from "../../util/http-common"

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
    user() {
      const config = {
        headers: {
          Authorization: `Token ${this.$cookies.get('auth-token')}`
        }
      }
      http
      .get("rest_auth/user/", config)
        .then(res => {
          console.log(res)
        })
        .catch(err => {
          console.log(err)
        })
    }

  },
  data: () => {
    return {
      pk: null,
      userInfo : {},
      userrank : [],
    };
  },
  created() {
    const config = {
      headers: {
        Authorization: `Token ${this.$cookies.get('auth-token')}`
      }
    }
    // pk 값 가져오는 요청
    http.get("rest_auth/user/", config)
    .then(res => {
      this.pk = res.data.pk

      // userInfo를 가져오는 요청
      http.post("accounts/userinfo/", { "pk": this.pk }, config)
      .then(re => {
        this.userInfo = re.data
      })
      .catch(err => {
        console.log(err)
      })

      // userrank를 가져오는 요청
      http.post("accounts/userrank/", { "pk": this.pk } ,config)
      .then(re => {
        this.userrank = re.data
      })
      .catch(err => {
        console.log(err)
      })
    })
    .catch(err => {
      console.log(err)
    })
  }
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