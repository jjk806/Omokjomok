import Vue from "vue";
import Router from "vue-router";

// 유저
import Login from "../page/user/Login.vue";
import Join from "../page/user/Join.vue";
import Mypage from "../page/user/Mypage.vue";

// 포스트
import Mainpage from "../page/post/Mainpage.vue";
import Game from "../page/post/Game.vue";
import RecentGame from "../page/post/RecentGame.vue";
import Rule from "../page/post/Rule.vue";

//곧 지울 테스트용 오목판 view 보러가기
import bigBoard from "../page/omokBoard/bigBoard.vue";
//기능별 오목판 view 들
import fightWithAI_bigBoard from "../page/board_fightWithAI/fightWithAI_bigBoard.vue";
import trickSolving_bigBoard from "../page/board_trickSolving/trickSolving_bigBoard.vue";


import TrickSolve from "../page/tricksolving/tricksolve.vue"


Vue.use(Router);

export default new Router({
  mode: 'history',
  routes: [
    // 로그인/가입
    {
      path: "/user/login",
      name: "Login",
      component: Login,
    },
    {
      path: "/user/join",
      name: "Join",
      component: Join,
    },
    {
      path: "/user/Mypage",
      name: "Mypage",
      component: Mypage,
    },

    // 포스트
    {
      path: "/",
      name: "Mainpage",
      component: Mainpage,
    },
    // 대국
    {
      path: "/post/Game",
      name: "Game",
      component: Game,
    },
    // 최근 대국
    {
      path: "/post/RecentGame",
      name: "RecentGame",
      component: RecentGame,
    },
    // 룰 설명 페이지
    {
      path: "/post/Rule",
      name: "Rule",
      component: Rule ,
    },
    //곧 지울 테스트용 오목판 이동
    {
      path: "/omokBoard/bigBoard",
      name: "bigBoard",
      component: bigBoard,
    },
    //AI 대결용 오목판 이동
    {
      path: "/board_fightWithAI/fightWithAI_bigBoard",
      name: "fightWithAI_bigBoard",
      component: fightWithAI_bigBoard,
    },
    //묘수풀이용 오목판 이동
    {
      path: "/board_trickSolving/trickSolving_bigBoard",
      name: "trickSolving_bigBoard",
      component: trickSolving_bigBoard,
    },    
    // 묘수 풀이
    {
      path: "/tricksolve",
      name: "TrickSolve",
      component: TrickSolve
    },

  ],
});
