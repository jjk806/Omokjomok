<template>
  <div
    class="p-10 text-center m-auto"
    v-if="matchRound1 && matchRound1.board && matchRound1.board.tab && matchRound1.board.tab.length"
  >
    <div
      class="row flex justify-center align-center p-0"
      v-for="(line, posY) in matchRound1.board.tab"
      :key="posY"
    >
      <div class="text-gray-600 w-5">{{ matchRound1.alphabet[posY] }}</div>
      <Tile
        v-for="(tile, posX) in line"
        :key="posX + matchRound1.board.tab.length * posY"
        :value="matchRound1.board.tab[posY][posX]"
        :posX="posX"
        :posY="posY"
        :isSuggestion="
          posY === matchRound1.suggestion.y && posX === matchRound1.suggestion.x
        "
        :anyMoveIsPending="!!matchRound1.pendingPosition"
        :isPendingPosition="
          !!matchRound1.pendingPosition &&
          posY === matchRound1.pendingPosition.y &&
          posX === matchRound1.pendingPosition.x
        "
      />
    </div>
  </div>
</template>

<script>
import { mapState } from "vuex";
import Tile from "./Tile.vue";

export default {
  name: "Board",
  components: { Tile },
  mounted() {
    // const { matchId } = this.match;
    // if (!this.$route.params.id)
    //   this.$router.push({ name: "match", params: { id: matchId } });

    console.log(this.matchRound1.board.tab[0]);
    console.log("board 도착");
  },
  methods: {},
  computed: {
    ...mapState(["matchRound1"]),
  },
};
</script>
