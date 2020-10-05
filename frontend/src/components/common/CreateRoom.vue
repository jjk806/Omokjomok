<template>
  <b-container>
    <b-modal
      id="modal-create-room"
      ref="modal"
      title="AI 대전 설정"
      centered
      hide-footer
      @show="resetModal"
      @hidden="resetModal"
      @ok="handleOk"
    >
      <form ref="form" @submit.stop.prevent="handleSubmit">
        <!-- checkbox -->
        <b-form-group>
          <b-form-group>
            <b-form-radio-group id="radio-group-2" v-model="selectOrder">
              <b-row>
                <b-col class="text-info" cols=3>공격 순서</b-col>
                <b-col cols=3>
                  <b-form-radio value="first">선공</b-form-radio>
                </b-col>
                <b-col>
                  <b-form-radio value="second">후공</b-form-radio>
                </b-col>
              </b-row>
            </b-form-radio-group>
          </b-form-group>

          
          <!-- <b-form-group>
            <b-form-radio-group
              id="radio-group-2"
              v-model="selectLevel"
            ></b-form-radio-group>
          </b-form-group> -->
          <b-form-group>
            <b-form-radio-group id="level" v-model="selectLevel">
              <b-row>
                <b-col class="text-info" cols=3>난이도</b-col>
                <b-col cols=3>
                  <b-form-radio value="high">상</b-form-radio>
                </b-col>
                <b-col cols=3>
                  <b-form-radio value="mid">중</b-form-radio>
                </b-col>
                <b-col cols=3>
                  <b-form-radio value="low">하</b-form-radio>
                </b-col>
              </b-row>
            </b-form-radio-group>
          </b-form-group>

          <b-row class="mt-5">
            <b-col>
              <b-button @click='initSetBoard' :to="{ name: 'bigBoard' }" block variant="primary">생성하기</b-button>
            </b-col>
          </b-row>
          <b-row class="mt-3">
            <b-col>
              <b-button block variant="danger">취소하기</b-button>
            </b-col>
          </b-row>
        </b-form-group>
      </form>
    </b-modal>
  </b-container>
</template>

<script>
import { mapActions } from "vuex";
export default {
  data() {
    return {
      selectOrder: null,
      selectLevel: null,
    }
  },
  // created() {
  //   axios.post(`${API_URL}study/mystudy/join?email=${this.email}`,  {
  //     headers: {
  //       "Content-Type": "application/json; charset=utf-8",
  //       'jwt-auth-token': sessionStorage.getItem('jwt-auth-token'),
  //       'user-email': sessionStorage.getItem('user-email')
  //     }
  //   })
  //   .then(res => {
  //     var resItem = res.data
  //     for (var i=0; i<resItem.length; i++) {
  //       this.check(resItem,i)
  //       if (resItem[i].mgrEmail === this.email) {
  //         this.makingStudy += 1
  //       }
  //     }
  //     this.items = resItem
  //     this.countStudy = resItem.length
  //   })
  //   .catch(err => {
  //     console.log(err)
  //   })
  // },
  methods: {
    ...mapActions(['initSetBoard']),
    resetModal() {},
    handleOk() {},
  },
}
</script>

<style>

</style>