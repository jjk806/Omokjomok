import Vue from "vue";
import Vuex from "vuex";
import { cloneDeep } from "lodash";
import http from "@/util/http-common";
import { mapState } from "vuex";

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
      size: 15,
      suggestedPosition: -1,
      //tab : null
      tab: [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
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
    makeMove(state, data) {
      state.match.board.tab = cloneDeep(data);
    },
    setmoveIsPending(state, { moveIsPending, posX, posY }) {
      state.match.pendingPosition = moveIsPending ? { x: posX, y: posY } : null;
    },
  },
  actions: {
    makeMove({ state, commit }, { posX, posY }) {
      commit("setmoveIsPending", { moveIsPending: true, posX, posY });
      console.log(this.state.match.board.tab);
      console.log(posX, posY);
      this.state.match.board.tab[posY][posX] = 2;
      //여기서 부터 커스텀
      http
        .post("/testgame/", { board: this.state.match.board.tab })
        .then(({ data }) => {
          if (data != null) {
            // this.match.board.tab = data;
            commit("makeMove", data);
          } else {
            alert(" <추후 수정>실패했습니다.");
          }
          console.log(data);
          //this.state.match.board.tab = data.cloneDeep;
          commit("setmoveIsPending", { moveIsPending: false, posX, posY });
        });
    },
  },
  computed: {
    ...mapState(["state"]),
  },
});
