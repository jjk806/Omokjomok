<template>
  <div id="header" v-if="isHeader">
    <b-container>
      <b-col cols="10">
        <b-button id="mainTitle" router :to="{ name: 'List' }" variant="white"
          >오 목 조 목</b-button
        >
      </b-col>
      <b-row>
        <b-col cols="1" align-self="center">
          <b-button-group>
            <b-dropdown size="lg" variant="link" left no-caret>
              <template v-slot:button-content>
                <b-icon scale="2" icon="justify"></b-icon>
                <span class="sr-only"></span>
              </template>
              <b-dropdown-item router :to="{ name: 'Mypage' }"
                >마이페이지</b-dropdown-item
              >
              <b-dropdown-item v-b-modal.modal-create-room
                >방 만들기</b-dropdown-item
              >
              <b-dropdown-item>친구와 대전</b-dropdown-item>
              <b-dropdown-item>AI 대전</b-dropdown-item>
              <b-dropdown-item router :to="{ name: 'bigBoard' }"
                >테스트용 오목판 view</b-dropdown-item
              >
              <b-dropdown-divider></b-dropdown-divider>
              <b-dropdown-item router :to="{ name: 'Login' }"
                >로그인</b-dropdown-item
              >
              <b-dropdown-item router :to="{ name: 'Game' }"
                >대국</b-dropdown-item
              >
              <b-dropdown-item router :to="{ name: 'RecentGame' }"
                >최근 대국</b-dropdown-item
              >
            </b-dropdown>
          </b-button-group>
        </b-col>
        <b-navbar
          toggleable="md"
          class="py-1 shadow-sm"
          type="light"
          variant="white"
        >
          <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>
          <b-navbar-nav
            class="w-100 justify-content-between"
            style="max-width: 1080px"
          >
            <b-nav-item to="/caselist">
              <b-icon icon="list"></b-icon>
              <span class>&nbsp;제보목록</span>
            </b-nav-item>
            <b-nav-item to="/reportinfo">
              <b-icon icon="bar-chart"></b-icon>
              <span>&nbsp;제보현황</span>
            </b-nav-item>
            <b-nav-item to="/mapmain">
              <b-icon icon="map"></b-icon>
              <span>&nbsp;지도보기</span>
            </b-nav-item>
            <b-nav-item to="/noticeboard">
              <b-icon icon="info-circle"></b-icon>
              <span>&nbsp;공지사항</span>
            </b-nav-item>
            <b-nav-item to="/howtouse">
              <b-icon icon="question-circle"></b-icon>
              <span>&nbsp;이용방법</span>
            </b-nav-item>
          </b-navbar-nav>
        </b-navbar>
      </b-row>
    </b-container>

    <b-modal
      id="modal-create-room"
      ref="modal"
      title="방 만들기"
      centered
      @show="resetModal"
      @hidden="resetModal"
      @ok="handleOk"
    >
      <form ref="form" @submit.stop.prevent="handleSubmit">
        <!-- roomTitle -->
        <b-form-group
          label="방 제목"
          label-for="roomTitle-input"
          invalid-feedback="Title is required"
          class="text-info"
        >
          <b-form-input
            id="roomTitle-input"
            v-model="roomTitle"
            placeholder="방 제목을 입력하세요"
            required
          ></b-form-input>
        </b-form-group>
        <!-- roomPASSWORD -->
        <b-form-group
          label="비밀번호"
          label-for="roomPassword-input"
          invalid-feedback="Password is required"
          class="text-info"
        >
          <b-form-input
            id="roomPassword-input"
            v-model="roomPassword"
            placeholder="방 비밀번호를 입력하세요"
            required
          ></b-form-input>
        </b-form-group>

        <!-- checkbox -->
        <b-form-group label="관전 허용" class="text-info">
          <b-row>
            <b-col>
              <b-form-checkbox
                id="checkbox-1"
                v-model="status"
                name="checkbox-1"
                value="accepted"
                class="text-dark"
                unchecked-value="not_accepted"
                >허용</b-form-checkbox
              >
            </b-col>
            <b-col>
              <b-form-checkbox
                id="checkbox-1"
                v-model="status"
                name="checkbox-1"
                value="accepted"
                class="text-dark"
                unchecked-value="not_accepted"
                >미허용</b-form-checkbox
              >
            </b-col>
          </b-row>
        </b-form-group>
      </form>
      <template v-slot:modal-footer="{ ok, cancel }">
        <!-- Emulate built in modal footer ok and cancel button actions -->
        <b-row>
          <b-col>
            <b-button size="sm" variant="danger" @click="cancel()"
              >CANCEL</b-button
            >
          </b-col>
          <b-col>
            <b-button size="sm" variant="success" @click="ok()"
              >SUBMIT</b-button
            >
          </b-col>
        </b-row>
      </template>
    </b-modal>
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
    clickCrateRoom() {},
    resetModal() {},
    handleOk() {},
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
</style>