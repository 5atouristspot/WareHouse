<template>
  <div id="GoBack" class="GoBack global-bg-color">
    <el-row>
      <el-col :span="24">
        <el-button plain icon="el-icon-arrow-left" @click="goBack(target)">返回</el-button>
      </el-col>
    </el-row>
  </div>
</template>
<script>
  export default {
    name: 'GoBack',
    props: {
      target: {
        type: String,
        default: ''
      },
    },
    methods: {
      goBack(target) {
        this.$router.push(target)
      }
    }
  }
</script>

<style lang="less" scoped>
.GoBack {
  padding: 30px;
  text-align: left;
  .el-button {
    width: 130px;
    height: 60px;
    font-size: 24px;
    border: 1px solid #888888;
  }
  .el-button:hover, .el-button:focus {
    border: 1px solid #666666;
    color: #333333;
  }
}
</style>
                    
