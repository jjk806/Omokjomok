<template>
  <div id="header" v-if="isHeader">
    <b-container fluid>
      <b-row align-v="center">
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
        <b-col offset="2" >
          <b-button id="mainTitle" router :to="{ name: 'Mainpage' }" variant="white">오 목 조 목</b-button>
        </b-col>
        <b-col cols=1>
          <b-link><b-icon @click="$bvModal.show('modal-scoped')" class="icon-size" icon="question-circle-fill" aria-label="Help"></b-icon></b-link>
        </b-col>
        <b-col cols=1>
          <b-link :to="{ name: 'Mypage' }"><b-icon class="icon-size" icon="person-fill" aria-label="Help"></b-icon></b-link>
        </b-col>
      </b-row>
    </b-container>

    <b-modal size="lg" centered id="modal-scoped">
      <template v-slot:modal-header="{ }">
        <!-- Emulate built in modal header close button action -->
        <h5>오목 규칙 TIP</h5>
      </template>

      <template v-slot:default="{ ok }">
        <b-container>
          <b-row>
            <b-col>
              <img src="../../assets/rule.png" alt="" width="1000px">
            </b-col>
          </b-row>
          <b-row class="mt-3">
            <b-col offset="9">
              <b-link @click="ok()" :to="{ name: 'Rule' }">규칙 더 보러가기</b-link>
            </b-col>
          </b-row>
        </b-container>

      </template>

      <template v-slot:modal-footer="{ ok }">
        <!-- Emulate built in modal footer ok and cancel button actions -->
        <b-button size="sm" variant="success" @click="ok()">
          닫기
        </b-button>
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
    clickTip() {
      // alert('꿀팁!')
      this.boxTwo = ''
      this.$bvModal.msgBoxOk('Data was submitted successfully', {
        title: '렌쥬룰 설명',
        size: 'lg',
        buttonSize: 'lg',
        okVariant: 'success',
        headerClass: 'p-2 border-bottom-0',
        footerClass: 'p-2 border-top-0',
        centered: true,
        src: '../../assets/rule.png',
      })
        .then(value => {
          this.boxTwo = value
        })
        .catch(err => {
          // An error occurred
        })
    },
    showMsgOk() {
      const h = this.$createElement
      // Using HTML string
      const titleVNode = h('div', { domProps: { innerHTML: '렌주룰 설명' } })
      // More complex structure
      const messageVNode = h('div', { class: ['foobar'] }, [
        h('p', { class: ['text-center'] }, [
          ' Flashy ',
          h('strong', 'msgBoxOk'),
          ' message ',
        ]),
        // h('p', { class: ['text-center'] }, [h('b-spinner')]),
        h('b-img', {
          props: {
            src: 'https://picsum.photos/id/20/250/250',
            alt: 'rule',
            // thumbnail: true,
            // center: true,
            // fluid: true, 
            // rounded: 'circle'
          }
        })
      ])
      // We must pass the generated VNodes as arrays
      this.$bvModal.msgBoxOk([messageVNode], {
        title: [titleVNode],
        buttonSize: 'sm',
        centered: true, size: 'sm'
      })
    }
  },
};
</script>


<style>
#header {
  height: 90px;
}
#mainTitle {
  font-size: xx-large;
}


.icon-size {
  font-size: 50px;
}
</style>