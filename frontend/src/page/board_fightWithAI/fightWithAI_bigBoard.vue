<template>
  <div class="h-full w-80-rem self-center flex flex-col p-10 text-white-whip">
    <Board
      v-if="match && match.board && match.board.tab && match.board.tab.length"
    />
  </div>
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
