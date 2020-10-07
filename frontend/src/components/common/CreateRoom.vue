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
            <b-form-radio-group id="whoAttack" v-model="selectOrder">
              <b-row>
                <b-col class="text-info" cols=3>공격 순서</b-col>
                <b-col cols=3>
                  <b-form-radio value="1">선공</b-form-radio>
                </b-col>
                <b-col>
                  <b-form-radio value="2">후공</b-form-radio>
                </b-col>
              </b-row>
            </b-form-radio-group>
          </b-form-group>

          <b-form-group>
            <b-form-radio-group id="level" v-model="selectLevel">
              <b-row>
                <b-col class="text-info" cols=3>난이도</b-col>
                <b-col cols=3>
                  <b-form-radio value="2">상</b-form-radio>
                </b-col>
                <b-col cols=3>
                  <b-form-radio value="1">중</b-form-radio>
                </b-col>
                <b-col cols=3>
                  <b-form-radio value="0">하</b-form-radio>
                </b-col>
              </b-row>
            </b-form-radio-group>
          </b-form-group>

          <b-row class="mt-5">
            <b-col>
              <b-button @click='createRoom()' :to="{ name: 'bigBoard' }" block variant="primary" class="text-light">생성하기</b-button>
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
import { mapState, mapActions } from "vuex";

import http from "../../util/http-common"

export default {
  data() {
    return {
      selectOrder: null,
      selectLevel: null,

    }
  },
  methods: {
    ...mapActions(['initSetBoard']),
    ...mapActions(["clearMatch"]),

    createRoom() {
      console.log('bbbbbbb')
      // pk 값을 이용해서 횟수를 늘리기 위한 요청
      const config = {
        headers: {
          Authorization: `Token ${this.$cookies.get('auth-token')}`
        }
      }
      // pk 값 가져오는 요청
      http.get("rest_auth/user/", config)
      .then(res => {
        var pk = res.data.pk
        console.log('aaaaaaaaaa')
        // userInfo를 가져오는 요청
        http.post("accounts/userplay/", { "pk": pk }, config)
        .then(() => {
          this.clearMatch();
          this.match.turn = this.selectOrder;
          this.match.level = this.selectLevel;

          if(this.match.turn != null && this.match.level != null){
            this.$router.push({ name: "fightWithAI_bigBoard"})
          }else{
            alert("공격순서와 난이도를 설정해주세요.");
          }
        })
        .catch(err => {
          console.log(err)
        })
        
      })
      .catch(err => {
        console.log(err)
      })
      
    },
    resetModal() {},
    handleOk() {},
  },
  computed: {
    ...mapState(["match"]),
  },
}
</script>

<style>

</style>