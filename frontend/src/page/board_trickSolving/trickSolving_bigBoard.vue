<template>
<b-container class ="p-20"> 
  <b-row>
    <b-col cols = "8">
      <div class="h-full self-center flex flex-col text-white-whip" >
        <Board
          v-if="match && match.board && match.board.tab && match.board.tab.length "
        />
      </div>
    </b-col>
    <b-col cols = "3">
      <div class="h-full">
        <b-container > 
          <b-row>
            <b-col cols = "4">p1</b-col>
            <b-col cols = "4">p2</b-col>
          </b-row>
          <b-row><p></p></b-row>
          <b-row><p></p></b-row>
          <b-row><p></p></b-row>
          <b-row><p></p></b-row>
          <b-row><p></p></b-row>
          <b-row>
            <b-col cols = "4">검은돌 차례</b-col>
            <b-col cols = "4">백돌 차례</b-col>
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
            <b-col cols = "4">
              <button
                class="btn"
                @click="undo"
              >무르기</button>
            </b-col>
            <b-col cols = "4">
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
  methods: {
    // local methods here
    undo() {},
    restartGame() {
      this.clearMatch();
      this.$router.push("/");
    },
    ...mapActions(["newMatch", "undoMove", "clearMatch"]),
  },
  computed: {
    // local computed here
    ...mapState(["match"]),
  },
};
</script>
