<template>
  <b-container id="loginCon" style="" >
    <h1 class="signup-title my-5">로그인</h1>
		<!-- 유저네임 -->
    <b-row class="my-3">
      <b-col>
        <b-form @submit.prevent="checkEmail">
          <b-input-group>
            <label
              style="text-align:right"
              for="input-large"
            ></label>
            <b-input-group-prepend variant is-text>
              <b-icon icon="person"></b-icon>
            </b-input-group-prepend>
            <b-form-input
              v-model="loginInfo.username"
							size="lg"
              type="email"
              required
              placeholder="유저이름을 입력해주세요"
            ></b-form-input>
          </b-input-group>
        </b-form>
      </b-col>
    </b-row>
    <!-- 이메일 -->
    <b-row class="my-3">
      <b-col>
        <b-form @submit.prevent="checkEmail">
          <b-input-group>
            <label
              style="text-align:right"
              for="input-large"
            ></label>
            <b-input-group-prepend variant is-text>
              <b-icon icon="person"></b-icon>
            </b-input-group-prepend>
            <b-form-input
              v-model="loginInfo.email"
							size="lg"
              type="email"
              required
              placeholder="이메일을 입력해주세요"
            ></b-form-input>
          </b-input-group>
        </b-form>
      </b-col>
    </b-row>
		<!-- 비밀번호 -->
		<b-row class="my-3">
			<b-col>
        <b-form>
          <b-input-group>
            <label
              style="text-align:right"
              for="input-large"
            ></label>
            <b-input-group-prepend variant is-text>
              <b-icon icon="unlock"></b-icon>
            </b-input-group-prepend>
            <b-form-input
              v-model="loginInfo.password"
							size="lg"
              type="password"
              required
              placeholder="비밀번호를 입력해주세요"
            ></b-form-input>
          </b-input-group>
        </b-form>
			</b-col>
		</b-row>
		<!-- 로그인 버튼 -->
		<b-row class="mt-5">
			<b-col>
				<b-button block size="lg" @click="login()">로그인</b-button>
			</b-col>
		</b-row>

		<!-- 회원가입 버튼 -->
		<b-row class="my-3">
			<b-col>
				<b-button v-b-modal.modal-prevent-closing block size="lg">회원가입</b-button>
			</b-col>
		</b-row>

		<b-modal
      id="modal-prevent-closing"
      ref="modal"
      title="회원가입"
			centered
      @show="resetModal"
      @hidden="resetModal"
      @ok="handleOk"
    >
      <form ref="form" @submit.stop.prevent="handleSubmit">
				<!-- ID -->
        <b-form-group
          :state="userIdState"
          label="ID"
          label-for="userId-input"
          invalid-feedback="ID is required"
        >
          <b-form-input
            id="userId-input"
            v-model="userId"
            :state="userIdState"
            required
          ></b-form-input>
        </b-form-group>
				<!-- PASSWORD -->
        <b-form-group
          :state="nameState"
          label="PASSWORD"
          label-for="password-input"
          invalid-feedback="Password is required"
        >
          <b-form-input
            id="password-input"
            v-model="password"
            :state="passwordState"
            required
          ></b-form-input>
        </b-form-group>
				<!-- EMAIL -->
        <b-form-group
          :state="nameState"
          label="EMAIL"
          label-for="email-input"
          invalid-feedback="Email is required"
        >
          <b-form-input
            id="email-input"
            v-model="email"
            :state="emailState"
            required
          ></b-form-input>
        </b-form-group>
      </form>
			<template v-slot:modal-footer="{ ok, cancel }">
				<!-- Emulate built in modal footer ok and cancel button actions -->
				<b-row>
					<b-col>
						<b-button size="sm" variant="danger" @click="cancel()">
							CANCEL
						</b-button>
					</b-col>
					<b-col>
						<b-button size="sm" variant="success" @click="ok()">
							SIGNUP
						</b-button>
					</b-col>
				</b-row>
			</template>
    </b-modal>

		<!-- 비밀번호 찾기 -->
		<b-row class="my-3">
			<b-col class="text-right">
				<router-link :to="{ name: 'Mainpage' }">비밀번호 찾기</router-link>
			</b-col>
		</b-row>
  </b-container>
</template>

<script>
import http from "@/util/http-common"

export default {
	name: "Login",
	data() {
		return {
			loginInfo: {
        username: null,
        email: null,
				password: null,
			},
			signupInfo: {
				userId: null,
				password: null,
				email: null
      },
      isLoggedIn: false
		}
	},
	methods: {
    setCookie(key) {
      this.$cookies.set('auth-token', key)
      this.isLoggedIn = true
    },
    login() {
      http
        .post("rest_auth/login/", this.loginInfo)
          .then(res => {
            this.setCookie(res.data.key)
            console.log(this.$cookies)
            this.$router.push('/')
          })
          .catch(err => {
            console.error(err)
            alert(err)
          })
    },
		signupModal() {
			this.$bvModal.msgBoxConfirm('signupForm()', {
				title: '회원가입',
				size: 'lg',
				buttonSize: 'lg',
				okVariant: 'success',
				okTitle: 'SIGNUP',
				cancelTitle: 'CANCEL',
				footerClass: 'p-2',
				hideHeaderClose: false,
				centered: true
			})
		},
		signupForm() {
			alert('aaa')
		},

	},
};
</script>

<style>
#loginCon {
	max-width: 600px;
	position: absolute;
	top: 25%;
	left: 34.5%;
}
</style>