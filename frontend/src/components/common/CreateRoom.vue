<template>
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
</template>

<script>
export default {
  created() {
    
  },
  methods: {
    resetModal() {},
    handleOk() {},
  },
}
</script>

<style>

</style>