<template>
  <b-container fluid>
    <b-row class="mt-2">
      <b-col offset=1 cols=4>
        <b-button variant="dark" block v-b-modal.modal-create-room>
          AI 대전
          <img src="../../assets/ai.jpg" alt="" class="my-2" style="height: auto; width: 100%;">
        </b-button>
      </b-col>
      <b-col cols=4>
        <b-button class="text-light" variant="dark" block router :to="{ name: 'FirstSelectStage' }">
          묘수 풀이
          <div>
            <img class="my-2" src="../../assets/myosu.png" alt="" style="height: auto; width: 100%;">

          </div>
          </b-button>
      </b-col>
      <b-col cols=2>
        <br><br>
        <b-row>
          <b-col class="text-left">
            <h4>{{ userInfo.email }} 정보</h4>
          </b-col>
        </b-row>
        <br>
        <b-row>
          <b-col class="text-left" style="border-style: outset; border-width: 3px;">전적</b-col>
          <b-col class="text-left" style="border-style: solid; border-width: 1px;">{{ userInfo.play}}전 {{ userInfo.win }}승 {{userInfo.play-userInfo.win }}패</b-col>
        </b-row>
        <b-row>
          <b-col class="text-left" style="border-style: outset; border-width: 3px;">승률</b-col>
          <b-col class="text-left" style="border-style: solid; border-width: 1px;">{{ userInfo.rate }} %</b-col>
        </b-row>
        <b-row>
          <b-col class="text-left" style="border-style: outset; border-width: 3px;">묘수풀이</b-col>
          <b-col class="text-left" style="border-style: solid; border-width: 1px;">{{ userInfo.score}} 점</b-col>
        </b-row>
        <b-row>
          <b-col class="text-left" style="border-style: outset; border-width: 3px;">기보</b-col>
          <b-col class="text-left" style="border-style: solid; border-width: 1px;"><a href="">보러가기</a></b-col>
        </b-row>
      </b-col>
    </b-row>
    <b-row class="mt-5">
      <b-col offset=1 cols=4>
        <b-button block>AI 대전 설명
          <AiCarousel  class="my-2"/>
        </b-button>
      </b-col>
      <b-col cols=4>
        <b-button block>묘수 풀이 설명
          <MyosuCarousel class="my-2"/>
        </b-button>
      </b-col>
      <b-col cols=2>
        <br><br><br><br><br><br><br><br>
        <b-row>
          <b-col class="text-left">
            <h4>실시간 순위</h4>
          </b-col>
        </b-row>
        <br>
        <b-row >
          <b-col cols="3" class="text-left" style="border-style: outset; border-width: 3px;">No.</b-col>
          <b-col cols="9" class="text-left" style="border-style: outset; border-width: 3px;">유저</b-col>
        </b-row>
        <b-row>
          <b-col cols="3" class="text-left" style="border-style: solid; border-width: 1px;">1</b-col>
          <b-col cols="9" class="text-left" style="border-style: solid; border-width: 1px;">{{ userrank[0] }}</b-col>
        </b-row>
        <b-row>
          <b-col cols="3" class="text-left" style="border-style: solid; border-width: 1px;">2</b-col>
          <b-col cols="9" class="text-left" style="border-style: solid; border-width: 1px;">{{ userrank[1] }}</b-col>
        </b-row>
        <b-row>
          <b-col cols="3" class="text-left" style="border-style: solid; border-width: 1px;">3</b-col>
          <b-col cols="9" class="text-left" style="border-style: solid; border-width: 1px;">{{ userrank[2] }}</b-col>
        </b-row>
        <b-row>
          <b-col cols="3" class="text-left" style="border-style: solid; border-width: 1px;">4</b-col>
          <b-col cols="9" class="text-left" style="border-style: solid; border-width: 1px;">{{ userrank[3] }}</b-col>
        </b-row>
        <b-row>
          <b-col cols="3" class="text-left" style="border-style: solid; border-width: 1px;">5</b-col>
          <b-col cols="9" class="text-left" style="border-style: solid; border-width: 1px;">{{ userrank[4] }}</b-col>
        </b-row>
      </b-col>
    </b-row>
    
  <!--  -->
  <CreateRoom />


  </b-container>
</template>

<script>
import AiCarousel from "../../components/common/AiCarousel.vue";
import MyosuCarousel from "../../components/common/MyosuCarousel.vue";
import Rating from "../../components/common/Rating.vue";
import MyInfo from "../../components/common/MyInfo.vue";
import CreateRoom from "../../components/common/CreateRoom.vue";
// import axios from "axios";

import http from "../../util/http-common"

export default {
  name: "Mainpage",
  components: {
    AiCarousel,
    MyosuCarousel,
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
    },
    

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
  /* width: 460px; */
  height: 270px !important;
}

</style>