<template>
  <div id="header" v-if="isHeader">
    <b-container fluid>
      <b-row align-v="center">
        <b-col offset="2" >
          <b-button id="mainTitle" router :to="{ name: 'Mainpage' }" variant="white">오 목 조 목</b-button>
        </b-col>
        <b-col cols=1>
          <b-link><b-icon @click="clickTip" class="icon-size" icon="question-circle-fill" aria-label="Help"></b-icon></b-link>
        </b-col>
        <b-col cols=1>
          <b-link :to="{ name: 'Mypage' }"><b-icon class="icon-size" icon="person-fill" aria-label="Help"></b-icon></b-link>
        </b-col>
      </b-row>
      <b-row>
        <b-col cols="1" align-self="center">
          <b-button-group>
            <b-dropdown size="lg" variant="link" left no-caret>
              <template v-slot:button-content>
                <b-icon scale="2" icon="justify"></b-icon>
                <span class="sr-only"></span>
              </template>
              <b-dropdown-item router :to="{ name: 'bigBoard' }"
                >테스트용 오목판 view</b-dropdown-item
              >
              <b-dropdown-divider></b-dropdown-divider>
              <b-dropdown-item router :to="{ name: 'Login' }"
                >로그인</b-dropdown-item
              >
            </b-dropdown>
          </b-button-group>
        </b-col>

      </b-row>
    </b-container>

  </div>
</template>   

<script>
export default {
  name: "Header",
  data: function () {
    return {
      keyword: "",
      roomTitle: null,
      roomPassword: null,
      status: null,
    };
  },
  components: {},
  props: ["isHeader"],
  computed: {},
  watch: {},
  created() {},
  methods: {
    clickTip() {
      alert('꿀팁!')
    },
  },
};
</script>


<style>
#header {
  height: 100px;
}
#mainTitle {
  font-size: xx-large;
}


.icon-size {
  font-size: 50px;
}
</style>