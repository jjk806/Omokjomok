<template>
  <b-container id="loginCon" style="" >
    <h1 class="signup-title my-5">로그인</h1>
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
          <label              
              v-if="!vaildLogin.email"
              class="text-danger align-middle m-0"
              style="text-align:right"
              for="input-large"
            >이메일이 올바르지 않습니다.</label>
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
          <label              
              v-if="!vaildLogin.password"
              class="text-danger align-middle m-0"
              style="text-align:right"
              for="input-large"
            >패스워드는 8자리 이상입니다.</label>
        </b-form>
        </b-form>
			</b-col>
		</b-row>
		<!-- 로그인 버튼 -->
		<b-row class="mt-5">
			<b-col>
				<b-button block size="lg" @click="login()" :disabled="!loginPossible">로그인</b-button>
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
    >
      <form ref="form" @submit.prevent="handleSubmit">
				<!-- EMAIL -->
        <b-form-group
          label="이메일"
          label-for="userEmail-input"
          invalid-feedback="EMAIL is required"
          class="mb-1"
        >
          <b-form-input
            id="userEmail-input"
            v-model="signupInfo.email"
            required
          ></b-form-input>
        </b-form-group>
        <b-button size="sm" variant="primary" @click="mail()">인증메일 발송</b-button>

        <b-form-group
          label="인증번호"
          label-for="Emailconfirmation"
          invalid-feedback="EMAIL is required"
          v-if="mailsubmit"
        >
          <b-form-input
            id="Emailconfirmation"
            v-model="emailconfirmation"
            required
          ></b-form-input>
        </b-form-group>

				<!-- PASSWORD -->
        <b-form-group
          label="패스워드"
          label-for="password-input"
          invalid-feedback="Password is required"
        >
          <b-form-input
            id="password-input"
            v-model="signupInfo.password1"
            required
          ></b-form-input>
        </b-form-group>
				<!-- PASSWORD2 -->
        <b-form-group
          label="패스워드확인"
          label-for="passwordconfirmation-input"
          invalid-feedback="Passord Confirmation is required"
        >
          <b-form-input
            id="password2-input"
            v-model="signupInfo.password2"
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
						<b-button size="sm" variant="success" @click="signup()">
							SIGNUP
						</b-button>
					</b-col>
				</b-row>
			</template>
    </b-modal>

		<!-- 비밀번호 찾기 -->
		<!-- <b-row class="my-3">
			<b-col class="text-right">
				<router-link :to="{ name: 'List' }">비밀번호 찾기</router-link>
			</b-col>
		</b-row> -->
  </b-container>
</template>

<script>
import http from "@/util/http-common"

export default {
	name: "Login",
	data() {
		return {
			loginInfo: {
        email: null,
				password: null,
			},
			signupInfo: {
        email: null,
				password1: null,
				password2: null
      },
      isLoggedIn: false,
      mailsubmit: false,
      mailauthentication: null,
      emailconfirmation: null,
      vaildLogin: {
        email: false,
        password: false,
      },
      loginPossible: false,
		}
	},
  watch: {
    loginInfo: {
      deep: true,
      handler() {                
          console.log('watch')
          this.validCheck(this.loginInfo) 
      }
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
            console.log(';aaaaaaaaaaaaaa')
            this.setCookie(res.data.key)
            this.$store.state.isloggedin = true
            this.$router.push({ name: "Mainpage"})
          })
          .catch(err => {
            console.error(err)
            alert(err)
          })
    },
    logout() {
      const config = {
        headers: {
          Authorization: `Token ${this.$cookies.get('auth-token')}`
        }
      }
      http
        .post("rest_auth/logout/")
          .then((res) => {
            this.$cookies.remove('auth-token')
            this.$store.state.isloggedin = false
            this.$router.push('/')
          })
          .catch(err => console.log(err))
      // http
      //   .post("rest_auth/logout/", null, config)
      //     .then(() => {
      //       console.log('hi')
      //       this.$cookies.remove('auth-token')
      //       this.isLoggedIn = false
      //       this.$router.push('/')
      //     })
      //     .catch(err => console.error(err))
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
    handlesubmit() {
      console.log(this.signupInfo)
    },
    signup() {
      if (this.emailconfirmation == this.mailauthentication) {
        http
          .post("rest_auth/registration/", this.signupInfo)
            .then(res => {
              this.signupInfo.email = null
              this.signupInfo.password1 = null
              this.signupInfo.password2 = null
              this.mailsubmit = null
              this.mailauthentication = null
            })
      } else {
        alert('인증번호 오류')
      }
    },
    mail() {
      this.mailsubmit = true
      http
        .post("accounts/emailAuth/", { email: this.signupInfo.email})
          .then(res => {
            if (res.data == 0) {
              alert('존재하는 이메일입니다.')
              this.signupInfo.email = null
              this.mailsubmit = null
            } else {
              this.mailauthentication = res.data
            }

          })
    },
    validCheck(model) {
      if (model.email.indexOf("@") != -1 && model.email.lastIndexOf(".") != -1) {
          this.vaildLogin.email = true
      } else {
          this.vaildLogin.email = false
      }
      if (model.password.length > 7) {
          this.vaildLogin.password = true
      } else {
          this.vaildLogin.password = false
      }
      if (this.vaildLogin.email && this.vaildLogin.password) {
          this.loginPossible = true
      } else {
          this.loginPossible = false
      }
    },
  },
  created() {
    this.$cookies.remove('auth-token')
    this.$router.push('/')
    this.$store.state.isloggedin = false
  }
};
</script>

<style>
#loginCon {
	max-width: 600px;
	top: 25%;
	left: 34.5%;
}
</style>
