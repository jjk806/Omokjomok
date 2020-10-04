<template>
<b-container > 
  <b-row>
    <b-col cols = 10>
      <div class="h-full w-80-rem self-center flex flex-col p-10 text-white-whip" >
        <Board
          v-if="match && match.board && match.board.tab && match.board.tab.length "
        />
      </div>
    </b-col>
    <b-col cols = 2>

      <!-- 여기부터 오른쪽 편 게임상황 + 버튼 작성  -->
            <div class="h-full w-1-rem self-center flex flex-col p-10 text-white-whip">
              <div class="py-3 flex justify-end mb-4">
                <div class="flex flex-col mr-10">
                  <p>p1 (black stones)</p>
                  <p>Captured stones: {{ parseInt(match.players.p1.captured) }}</p>
                </div>
                <div class="flex flex-col mr-10">
                  <p>p2 (white stones)</p>
                  <p>Captured stones: {{ parseInt(match.players.p2.captured) }}</p>
                </div>
              </div>
              <div class="flex flex-wrap">
                  <button
                    class="btn"
                    @click="undoMove"
                    :disabled="match.moveIsPending || match.history === null || match.history.length === 0"
                  >Undo</button>
                </div>
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
    undoMove() {},
    localClearMatch() {
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
<style>
.Board{
  display : inline;
}
</style>