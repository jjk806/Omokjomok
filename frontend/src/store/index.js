import Vue from "vue";
import Vuex from "vuex";
import { cloneDeep } from "lodash";

Vue.use(Vuex);

const initialState = {
  message: "ASD1",
  errorResponse: "",
  httpEndpoint: process.env.VUE_APP_SERVER_HTTP || "http://localhost:4242",
  match: {
    // matchPending: undefined, // bool
    matchPending: false, // bool
    pendingPosition: null, // { x: int, y: int }
    // matchId: -1,
    matchId: 1,
    // currentPlayerId: -1,
    currentPlayerId: 2,
    suggestionTimer: 0,
    suggestorOn: undefined,
    suggestion: {
      x: -1,
      y: -1,
    },
    history: null,
    board: {
      size: 19,
      suggestedPosition: -1,
      //tab : null
      tab: [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
      ],
      invalidMoves: [], // returned with prev move
    },
    players: {
      p1: {
        isAi: false,
        id: 1,
        captured: 0,
      },
      p2: {
        isAi: false,
        id: 2,
        captured: 0,
      },
    },
  },
};
const API_URL = process.env.VUE_APP_LOCAL_URL;
export default new Vuex.Store({
  // state: {
  //   omokInfo: cloneDeep(initialState),
  // },
  state: cloneDeep(initialState),
  getters: {},
  mutations: {
    setmoveIsPending(state, { moveIsPending, posX, posY }) {
      state.match.pendingPosition = moveIsPending ? { x: posX, y: posY } : null;
    },
  },
  actions: {
    makeMove({ state, commit }, { posX, posY }) {
      commit("setmoveIsPending", { moveIsPending: true, posX, posY });
      console.info(`Making move at ${[posX, posY]}`);
      const url = new URL(
        `${state.httpEndpoint}/match/${state.match.matchId}/move`
      );
      const options = {
        method: "POST",
        cache: "no-cache",
        body: JSON.stringify({
          id: state.match.matchId,
          playerId: state.match.currentPlayerId,
          posX,
          posY,
        }),
      };
      // return fetch(url, options)
      //   .then((response) => response.json())
      //   .then((data) => {
      //     commit("makeMove", data);
      //   })
      //   .catch(() => {
      //     commit(
      //       "setError",
      //       `Could not make move for player ${state.match.currentPlayerId} at position x: ${posX}, y: ${posY}.`
      //     );
      //   })
      //   .finally(() => {
      //     commit("setmoveIsPending", { moveIsPending: false, posX, posY });
      //   });
    },
  },
});
