import Vue from "vue";
import Router from "vue-router";
import store from "../store/index.js"

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
// import bigBoard from "../page/omokBoard/bigBoard.vue";
//기능별 오목판 view 들
import fightWithAI_bigBoard from "../page/board_fightWithAI/fightWithAI_bigBoard.vue";
import trickSolving_bigBoard from "../page/board_trickSolving/trickSolving_bigBoard.vue";


// 묘수 풀이 페이지
import TrickSolveWun from "../page/tricksolving/tricksolvewun.vue"
import TrickSolvePo from "../page/tricksolving/tricksolvepo.vue"
import TrickSolveWha from "../page/tricksolving/tricksolvewha.vue"
import FirstSelectStage from "../page/tricksolving/FirstSelectStage.vue";

Vue.use(Router);

const requireAuth = () => (to, from, next) => {
  console.log(store.state.isloggedin)
  if (store.state.isloggedin) {
    return next();
  }
  next('/');
}


export default new Router({
  mode: 'history',
  routes: [
    // 로그인/가입
    {
      path: "/",
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
      beforeEnter: requireAuth()
    },

    // 포스트
    {
      path: "/home",
      name: "Mainpage",
      component: Mainpage,
      beforeEnter: requireAuth()
    },
    // 대국
    {
      path: "/post/Game",
      name: "Game",
      component: Game,
      beforeEnter: requireAuth()
    },
    // 최근 대국
    {
      path: "/post/RecentGame",
      name: "RecentGame",
      component: RecentGame,
      beforeEnter: requireAuth()
    },
    // 룰 설명 페이지
    {
      path: "/post/Rule",
      name: "Rule",
      component: Rule ,
      beforeEnter: requireAuth()
    },
    //곧 지울 테스트용 오목판 이동
    // {
    //   path: "/omokBoard/bigBoard",
    //   name: "bigBoard",
    //   component: bigBoard,
    //   beforeEnter: requireAuth()
    // },
    //AI 대결용 오목판 이동
    {
      path: "/fightWithAI_bigBoard",
      name: "fightWithAI_bigBoard",
      component: fightWithAI_bigBoard,
      beforeEnter: requireAuth()
    },
    //묘수풀이용 오목판 이동
    {
      path: "/trickSolving_bigBoard",
      name: "trickSolving_bigBoard",
      component: trickSolving_bigBoard,
      beforeEnter: requireAuth()
    },    
    // 묘수 풀이 종류 선택창
    {
      path: "/FirstSelectStage",
      name: "FirstSelectStage",
      component: FirstSelectStage,
      beforeEnter: requireAuth()
    },
    // 묘수 풀이 운월
    {
      path: "/tricksolvewun",
      name: "TrickSolveWun",
      component: TrickSolveWun,
      beforeEnter: requireAuth()
    },
    // 묘수 풀이 포월
    {
      path: "/tricksolvepo",
      name: "TrickSolvePo",
      component: TrickSolvePo,
      beforeEnter: requireAuth()
    },
    // 묘수 풀이 화월
    {
      path: "/tricksolvewha",
      name: "TrickSolveWha",
      component: TrickSolveWha,
      beforeEnter: requireAuth()
    },

  ],
});
