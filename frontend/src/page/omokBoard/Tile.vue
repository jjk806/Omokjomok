<template>
  <div
    class="flex-none flex flex-wrap justify-center items-center resize-none m-0 p-0 h-8 w-8 border-solid border-dark border rounded-sm content-center"
    :class="[
      { 'cursor-pointer': !anyMoveIsPending && value === 0 },
      { 'opacity-75 cursor-default': anyMoveIsPending },
      isSuggestion && !anyMoveIsPending ? 'bg-warning-70' : 'bg-orange-400',
    ]"
    @click="() => !anyMoveIsPending && value === 0 && sendMove({ posX, posY })"
    @mouseover="mouseOver"
    @mouseleave="mouseOut"
  >
    <div v-if="posY === 0" class="text-gray-600 -mt-12">{{ posX }}</div>
    <div class="h-3 w-3 p-3 rounded-full" :class="[stoneColor, stoneOpacity]" />
  </div>
</template>

<script>
import { mapState, mapActions } from "vuex";

export default {
  name: "Tile",
  props: {
    value: Number,
    posX: Number,
    posY: Number,
    isSuggestion: Boolean,
    anyMoveIsPending: {
      type: Boolean,
      default: false,
    },
    isPendingPosition: Boolean,
  },
  data() {
    return {
      hovering: false,
    };
  },
  computed: {
    stoneColor() {
      const {
        value,
        hovering,
        isSuggestion,
        match: { currentPlayerId: id },
      } = this;

      return !hovering && value === 0 && !isSuggestion
        ? ""
        : value === 1 || (value === 0 && (hovering || isSuggestion) && id === 1)
        ? "bg-black"
        : value === 2 || (value === 0 && (hovering || isSuggestion) && id === 2)
        ? "bg-white-whip"
        : "";
    },
    stoneOpacity() {
      const {
        value,
        hovering,
        isSuggestion,
        anyMoveIsPending,
        isPendingPosition,
      } = this;
      return value === 0 &&
        !isPendingPosition &&
        ((anyMoveIsPending && !isPendingPosition) ||
          (!hovering && !isSuggestion))
        ? "opacity-0"
        : isPendingPosition ||
          value > 0 ||
          (!anyMoveIsPending && hovering && isSuggestion)
        ? "opacity-100"
        : "opacity-50";
    },
    ...mapState(["match"]),
  },
  methods: {
    mouseOver() {
      this.hovering = true;
    },
    mouseOut() {
      this.hovering = false;
    },
    sendMove({ posX, posY }) {
      console.log("sendMove 시작!");
      this.makeMove({ posX, posY });
      console.log("sendMove 끝!");
    },
    ...mapActions(["makeMove"]),
  },
};
</script>
