<template>
  <b-container>
    <br><br>
    <div class="mt-5">
      <b-row>        
        <b-col cols="12" id="mypageInfo">
          <div id="userInfoList" >
            <b-row>
              <b-col md="3" offset-md="1" class="text-left font-weight-bold">이메일</b-col>
              <b-col md="3" offset-md="3" class="text-right font-weight-bold">{{ userInfo.email }}</b-col>
            </b-row>
            <hr>
            <b-row>
              <b-col md="3" offset-md="1" class="text-left font-weight-bold">승률</b-col>
              <b-col md="3" offset-md="3" class="text-right font-weight-bold">{{ userInfo.rate }} % </b-col>
              <b-col md="3" offset-md="1" class="text-left font-weight-bold">플레이횟수</b-col>
              <b-col md="3" offset-md="3" class="text-right font-weight-bold">{{ userInfo.play }}</b-col>
              <b-col md="3" offset-md="1" class="text-left font-weight-bold">승리</b-col>
              <b-col md="3" offset-md="3" class="text-right font-weight-bold">{{ userInfo.win }}</b-col>
            </b-row>
            <hr>
            <b-row>
              <b-col md="3" offset-md="1" class="text-left font-weight-bold">묘수풀이 점수</b-col>
              <b-col md="3" offset-md="3" class="text-right font-weight-bold">{{ userInfo.score }}</b-col>
            </b-row>
          </div>
        </b-col>
      </b-row>
      <hr />
      <div>
        <b-tabs content-class="mt-3" justified>
          <b-tab title="AI 대전" active>
            <p>AI 대전</p>
            <b-row>
              <table class="table table-striped">
                <thead>
                  <tr>
                    <th scope="col">게임시각</th>
                    <th scope="col">AI레벨</th>
                    <th scope="col">선/후공</th>
                    <th scope="col">승패</th>
                  </tr>
                </thead>
                <tbody>
                  <tr v-for="Recode in Watchlist">
                    <th scope="row">{{ Recode.created_at }}</th>
                    <td>{{ Recode.ailevel }}</td>
                    <td>{{ Recode.turn }}</td>
                    <td>{{ Recode.win }}</td>
                  </tr>
                </tbody>
              </table>
            </b-row>
            <br />
            <b-row>
              <b-col>
                <b-pagination
                  v-model="currentPage"
                  :total-rows="rows"
                  :per-page="perPage"
                  aria-controls="my-table"
                  align="center"
                ></b-pagination>
              </b-col>
            </b-row>
          </b-tab>
          <b-tab title="묘수풀이">
            <p>묘수풀이</p>
            <b-row>
              <table class="table table-bordered">
                <thead>
                  <tr>
                    <th scope="col">유형</th>
                    <th scope="col">1단계</th>
                    <th scope="col">2단계</th>
                    <th scope="col">3단계</th>
                    <th scope="col">4단계</th>
                    <th scope="col">5단계</th>
                  </tr>
                </thead>
                <tbody>
                  <tr>
                    <th scope="row">포월</th>
                    <td><div v-if="myosu[0]" class="text-danger">Clear!</div><div v-if="!myosu[0]">도전하세요</div></td>
                    <td><div v-if="myosu[1]" class="text-danger">Clear!</div><div v-if="!myosu[1]">도전하세요</div></td>
                    <td><div v-if="myosu[2]" class="text-danger">Clear!</div><div v-if="!myosu[2]">도전하세요</div></td>
                    <td><div v-if="myosu[3]" class="text-danger">Clear!</div><div v-if="!myosu[3]">도전하세요</div></td>
                    <td><div v-if="myosu[4]" class="text-danger">Clear!</div><div v-if="!myosu[4]">도전하세요</div></td>
                  </tr>
                  <tr>
                    <th scope="row">화월</th>
                    <td><div v-if="myosu[5]" class="text-danger">Clear!</div><div v-if="!myosu[5]">도전하세요</div></td>
                    <td><div v-if="myosu[6]" class="text-danger">Clear!</div><div v-if="!myosu[6]">도전하세요</div></td>
                    <td><div v-if="myosu[7]" class="text-danger">Clear!</div><div v-if="!myosu[7]">도전하세요</div></td>
                    <td><div v-if="myosu[8]" class="text-danger">Clear!</div><div v-if="!myosu[8]">도전하세요</div></td>
                    <td><div v-if="myosu[9]" class="text-danger">Clear!</div><div v-if="!myosu[9]">도전하세요</div></td>
                  </tr>
                  <tr>
                    <th scope="row">운월</th>
                    <td><div v-if="myosu[10]" class="text-danger">Clear!</div><div v-if="!myosu[10]">도전하세요</div></td>
                    <td><div v-if="myosu[11]" class="text-danger">Clear!</div><div v-if="!myosu[11]">도전하세요</div></td>
                    <td><div v-if="myosu[12]" class="text-danger">Clear!</div><div v-if="!myosu[12]">도전하세요</div></td>
                    <td><div v-if="myosu[13]" class="text-danger">Clear!</div><div v-if="!myosu[13]">도전하세요</div></td>
                    <td><div v-if="myosu[14]" class="text-danger">Clear!</div><div v-if="!myosu[14]">도전하세요</div></td>
                  </tr>
                </tbody>
              </table>
            </b-row>
          </b-tab>
        </b-tabs>
      </div>
    </div>
  </b-container>
</template>

<script>
import http from "../../util/http-common"

export default {
  name: "Mypage",
  data() {
    return {
      userInfo: Object,
      Recodelist: [],
      Watchlist: [],
      myosu: [],
      defaultImageUrl:
        "https://previews.123rf.com/images/salamatik/salamatik1801/salamatik180100019/92979836-%ED%94%84%EB%A1%9C%ED%95%84-%EC%9D%B5%EB%AA%85%EC%9D%98-%EC%96%BC%EA%B5%B4-%EC%95%84%EC%9D%B4%EC%BD%98-%ED%9A%8C%EC%83%89-%EC%8B%A4%EB%A3%A8%EC%97%A3-%EC%82%AC%EB%9E%8C%EC%9E%85%EB%8B%88%EB%8B%A4-%EB%82%A8%EC%84%B1-%EA%B8%B0%EB%B3%B8-%EC%95%84%EB%B0%94%ED%83%80-%EC%82%AC%EC%A7%84-%EC%9E%90%EB%A6%AC-%ED%91%9C%EC%8B%9C-%EC%9E%90-%ED%9D%B0%EC%83%89-%EB%B0%B0%EA%B2%BD%EC%97%90-%EA%B3%A0%EB%A6%BD-%EB%B2%A1%ED%84%B0-%EC%9D%BC%EB%9F%AC%EC%8A%A4%ED%8A%B8-%EB%A0%88%EC%9D%B4-%EC%85%98.jpg",

      perPage: 5,
      currentPage: 1,
      items: [
        { id: 1, first_name: "Fred", last_name: "Flintstone" },
        { id: 2, first_name: "Wilma", last_name: "Flintstone" },
        { id: 3, first_name: "Barney", last_name: "Rubble" },
        { id: 4, first_name: "Betty", last_name: "Rubble" },
        { id: 5, first_name: "Pebbles", last_name: "Flintstone" },
        { id: 6, first_name: "Bamm Bamm", last_name: "Rubble" },
        { id: 7, first_name: "The Great", last_name: "Gazzoo" },
        { id: 8, first_name: "Rockhead", last_name: "Slate" },
        { id: 9, first_name: "Pearl", last_name: "Slaghoople" },
      ],
    };
  },
  watch: {
    currentPage: {
      handler() {
          this.watchchange(this.currentPage) 
      }
    }
  },
  computed: {
    rows() {
      return this.Recodelist.length;
    },
  },
  methods: {
    watchchange(page) {
      this.Watchlist = this.Recodelist.slice((page-1)*5,page*5)
    },
  },
  created() {
    const config = {
      headers: {
        Authorization: `Token ${this.$cookies.get('auth-token')}`
      }
    }
    http.get("rest_auth/user/", config)
      .then(res => {
        var pk = res.data.pk
        http.post("accounts/userinfo/", { "pk": pk }, config)
          .then(re => {
            this.userInfo = re.data
          })
          .catch(err => {
            console.log(err)
          })
        http.post("omok_game/readallmyrecode/", { "pk": pk })
          .then(re => {
            this.Recodelist = re.data
            for(var i = 0; i < this.Recodelist.length; i++) {
              var created_at = String(this.Recodelist[i].created_at)
              this.Recodelist[i].created_at = created_at.substr(0,10) + " " + created_at.substr(11,8)
              if (this.Recodelist[i].ailevel == 1) {
                this.Recodelist[i].ailevel = "하"
              } else if (this.Recodelist[i].ailevel == 2) {
                this.Recodelist[i].ailevel = "중"
              } else if (this.Recodelist[i].ailevel == 3) {
                this.Recodelist[i].ailevel = "상"
              }
              if (this.Recodelist[i].turn == 1) {
                this.Recodelist[i].turn = "선공"
              } else if (this.Recodelist[i].turn == 2) {
                this.Recodelist[i].turn = "후공"
              }
              if (this.Recodelist[i].win) {
                this.Recodelist[i].win = "승"
              } else {
                this.Recodelist[i].win = "패"
              }
            }
            this.Watchlist = this.Recodelist.slice(0,5)            
          })
          .catch(err => {
            console.log(err)
          })
          http.post("omok_game/tricklist/", { "pk": pk })
          .then(re => {
            this.myosu = re.data
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

<style>
.post-img {
  height: 300px;
}
</style>
