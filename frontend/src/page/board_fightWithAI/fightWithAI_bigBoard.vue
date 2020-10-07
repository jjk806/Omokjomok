<template>
<b-container class ="p-20"> 

  <b-modal ref="my-modal" hide-footer hide-header>
    <!-- <div class="d-flex justify-content-around"> -->
    <div>
      <b-row class="justify-content-md-center">
        <img id="victory_icon" src="@/assets/img/gameEnd/win.png" />
      </b-row>
      <b-row class="justify-content-md-center">
        <b-col id = "difficult">
          AI 난이도 상
        </b-col>
      </b-row>
      <b-row class="justify-content-md-center">
        <b-col>
          홍길동 흑돌
        </b-col>
      </b-row>
      <b-row class="justify-content-md-center">
        <b-col>
          32수
        </b-col>
      </b-row>
      <b-row class="justify-content-md-center">
        <b-col>
          승리
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
            <b-col cols = "">p1</b-col>
            <b-col cols = "">p2</b-col>
          </b-row>
          <b-row><p></p></b-row>
          <b-row><p></p></b-row>
          <b-row><p></p></b-row>
          <b-row><p></p></b-row>
          <b-row><p></p></b-row>
          <b-row>
            <b-col cols = "">검은돌 차례</b-col>
            <b-col cols = "">백돌 차례</b-col>
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
                @click="undo"
              >무르기</button>
            </b-col>
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

export default {
  name: "Match",
  components: { Board },
  data: function () {
    return {
      showModal : false,
    };
  },
  methods: {
    // local methods here
    undo() {},
    restartGame() {
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
    if(this.match.gameEnd){
      alert("update 도착")
      this.showModal = true;
      alert(this.showModal)
      this.$refs['my-modal'].show()
    }
  },
};
</script>
<style scoped>
#forColor{
  background-color: #F2F2F2;
}
.col{
  text-align: center;
  font-size: 60px;
}
#difficult{
  font-size: 80px !important;
}
</style>