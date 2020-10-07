<template>
<b-container class ="p-20"> 
  <br><br><br><br><br><br><br>
  <b-modal ref="win-modal" hide-footer hide-header id= "win_modal">
    <!-- <div class="d-flex justify-content-around"> -->
    <div>
      <b-row class="justify-content-md-center">
        <img id="victory_icon" src="@/assets/img/gameEnd/win.png" />
      </b-row>
      <b-row class="justify-content-md-center">
        <b-col id = "difficult">
            <p v-if="this.match.level == 0">AI 난이도 하</p>
            <p v-if="this.match.level == 1">AI 난이도 중</p>
            <p v-if="this.match.level == 2">AI 난이도 상</p>
        </b-col>
      </b-row>
      <b-row class="justify-content-md-center">
        <b-col>
            <p v-if="this.match.currentPlayerId == 1">흑돌</p>
            <p v-if="this.match.currentPlayerId == 2">백돌</p>
        </b-col>
      </b-row>
      <b-row class="justify-content-md-center">
        <b-col>
          <p>{{this.match.board.stackIndex}} 수</p>
        </b-col>
      </b-row>
      <b-row class="justify-content-md-center">
        <b-col>
          승리
        </b-col>
      </b-row>
    </div>
  </b-modal>

  <b-modal ref="lose-modal" hide-footer hide-header id= "lose_modal">
    <!-- <div class="d-flex justify-content-around"> -->
    <div>
      <b-row class="justify-content-md-center">
        <img id="victory_icon" src="@/assets/img/gameEnd/lose.png" />
      </b-row>
      <b-row class="justify-content-md-center">
        <b-col id = "difficult">
            <p v-if="this.match.level == 0">AI 난이도 하</p>
            <p v-if="this.match.level == 1">AI 난이도 중</p>
            <p v-if="this.match.level == 2">AI 난이도 상</p>
        </b-col>
      </b-row>
      <b-row class="justify-content-md-center">
        <b-col>
            <p v-if="this.match.currentPlayerId == 1">흑돌</p>
            <p v-if="this.match.currentPlayerId == 2">백돌</p>
        </b-col>
      </b-row>
      <b-row class="justify-content-md-center">
        <b-col>
          <p>{{this.match.board.stackIndex}} 수</p>
        </b-col>
      </b-row>
      <b-row class="justify-content-md-center">
        <b-col>
          패배
        </b-col>
      </b-row>
    </div>
  </b-modal>

  <b-row>
    <b-col cols = "8">
      <div class="h-full self-center flex flex-col text-white-whip" >
        <Board
          v-if="match && match.board && match.board.tab && match.board.tab.length "
        />
      </div>
    </b-col>
    <b-col cols = "3" id = "forColor"> 
      <div class="h-full">
        <b-container > 
          <b-row>
            <b-col cols = "">흑돌</b-col>
            <b-col cols = "">백돌</b-col>
          </b-row>
          <b-row><p></p></b-row>
          <b-row><p></p></b-row>
          <b-row><p></p></b-row>
          <b-row><p></p></b-row>
          <b-row><p></p></b-row>
          <b-row>
            <b-col v-if="this.match.nowTurn == 1">당신 차례</b-col>
            <b-col v-if="this.match.nowTurn == 1"></b-col>
            <b-col v-if="this.match.nowTurn == 2"></b-col>
            <b-col v-if="this.match.nowTurn == 2">AI 차례</b-col>
          </b-row>
          <b-row><p></p></b-row>

          <b-row><p></p></b-row>
          <b-row><p></p></b-row>
          <b-row><p></p></b-row>
          <b-row><p></p></b-row>
          <b-row><p></p></b-row>
          <b-row><p></p></b-row>
          <b-row><p></p></b-row>
          <b-row><p></p></b-row>
          <b-row><p></p></b-row>
          <b-row><p></p></b-row>
          <b-row><p></p></b-row>
          <b-row><p></p></b-row>
          <b-row><p></p></b-row>
          <b-row><p></p></b-row>
          <b-row><p></p></b-row>
          <b-row><p></p></b-row>
          <b-row><p></p></b-row>
          <b-row><p></p></b-row>
          <b-row><p></p></b-row>

          <b-row>
            <b-col cols = "">
              <button
                class="btn"
                @click="restartGame"
              >재시작</button>
            </b-col>
          </b-row>
        </b-container > 
      </div>
      <!-- 여기까지 오른쪽 편 게임상황 + 버튼 작성  -->
    </b-col>
  </b-row>
</b-container>
</template>

<script>
import { mapState, mapActions } from "vuex";
import Board from "./Board.vue";
import http from "../../util/http-common"

export default {
  name: "Match",
  components: { Board },
  data: function () {
    return {
      posX : 0,
      poxY : 0,
    };
  },
  methods: {
    // local methods here
    undo() {},
    restartGame() {
      // pk 값 가져오는 요청
      const config = {
        headers: {
          Authorization: `Token ${this.$cookies.get('auth-token')}`
        }
      }
      http.get("rest_auth/user/", config)
      .then(res => {
        var pk = res.data.pk

        // userInfo를 가져오는 요청
        http.post("accounts/userplay/", { "pk": pk }, config)
        .catch(err => {
          console.log(err)
        })
        
      })
      .catch(err => {
        console.log(err)
      })
      const tempTurn = this.match.turn;
      const tempLevel = this.match.level;
      this.clearMatch();
      this.match.level = tempLevel;
      this.match.turn = tempTurn;
      if(this.match.turn == 1){
        this.match.currentPlayerId = 1;
      }
      if(this.match.turn == 2){
        this.justSendOne();
        this.match.currentPlayerId = 2;
      }
      // this.$router.push("/fightWithAI_bigBoard");
      // this.$router.push(this.$router.currentRoute);
      this.$router.push("/fightWithAI_bigBoard").catch(()=>{});
      // router.push("/", () => {});
    },
    ...mapActions(["newMatch", "undoMove", "clearMatch", "justSendOne"]),
  },
  computed: {
    // local computed here
    ...mapState(["match"]),
  },
  mounted(){
    if(this.match.turn == 1){
      this.match.currentPlayerId = 1;
    }
    if(this.match.turn == 2){
      this.justSendOne();
      this.match.currentPlayerId = 2;
    }
  },
  updated(){

    if(this.match.nowTurn == 1){
      this.match.nowWeCanMove = true;
    }
    if(this.match.amIWin == true){
      // 이기는 횟수 요청
      // pk 값 가져오는 요청
      http.get("rest_auth/user/", config)
      .then(res => {
        var pk = res.data.pk

        // userInfo를 가져오는 요청
        http.post("accounts/userwin/", { "pk": pk }, config)
        .then(() =>{
          this.$refs['win-modal'].show()
        })
        .catch(err => {
          console.log(err)
        })
        
      })
      .catch(err => {
        console.log(err)
      })
      // this.$router.push("/")
    }
    // 경기 짐
    else if(this.match.amIWin == false){
      this.$refs['lose-modal'].show()
    }
  },
};
</script>
<style scoped>
#forColor{
  background-color: #F2F2F2;
}
#win_modal .col{
  text-align: center;
  font-size: 40px;
}
#lose_modal .col{
  text-align: center;
  font-size: 40px;
}
#difficult{
  font-size: 80px !important;
}
</style>