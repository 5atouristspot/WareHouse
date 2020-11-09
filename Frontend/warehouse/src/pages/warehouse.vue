<template>
  <div id="warehouse global-bg-color">
    <GoBack v-bind:target="target"/>
    <div class="top-div global-bg-color">
      <el-row style="width: 100%">
        <el-col :span="(index > 0 && index == utilizationRateList.length - 1) ? 6 : 3" v-for="(item, index) in utilizationRateList" :key="index">
          <el-row v-for="(subItem, subIndex) in item.list" :key="subIndex" class="item-row">
            <el-col :span="15" class="subItem-left-col"><div>{{subIndex}}</div></el-col>
            <el-col :span="9" class="subItem-right-col"><div :class="{'green':subIndex === specialKey}">{{item.list[subIndex]}}</div></el-col>
          </el-row>
        </el-col>
      </el-row>
    </div>

    <div v-if="type === '1'">
      <div class="special-content-div global-bg-color tl">
        <el-row v-for="(item, index) in storagebinList" :key="index" class="storage-col">
          <el-col class="storage-left-col">{{item.name}}</el-col>
          <el-col class="storage-right-col">
          <span v-for="(subItem, subIndex) in item.list" :key="subIndex">
            <br v-if="isShowBr(item, subIndex)">
            <div class="div-null" v-if="isShowNullDiv(item, subIndex)"></div>
            <el-button class="storage-item-btn"
                       :class="btnClass(subItem.status)"
                       @click="redirect(subItem.name, subItem.status)">
              {{subItem.name}}
            </el-button>
          </span>
          </el-col>
        </el-row>
      </div>
    </div>
    <div v-else>
      <div class="content-div global-bg-color tl">
        <el-row style="width: 100%" :gutter="10">
          <el-col :span="4" v-for="(item, index) in storagebinList" :key="index" style="margin-bottom: 10px">
            <el-button class="storagebin-btn"
                       :class="btnClass(item.status)"
                       @click="redirect(item.name)">
              {{item.name}}
            </el-button>
          </el-col>
        </el-row>
      </div>
    </div>

  </div>
</template>

<script>
  import GoBack from '@/components/GoBack'
  export default {
    name: 'warehouse',
    data() {
      return {
        target: '/plan',
        utilizationRateList: [],
        storagebinList: [],
        type: '',
        specialKey: '使用率',
        specialArray: ['02-05', '02-04', '02-03', '03-05', '03-04', '03-03', '05-05', '05-04', '05-03']
      }
    },
    methods: {
      init() {
        this.type = this.$route.params.type
        let reqParams = {
          warehouse_type: this.type
        }
        this.$axios.defaults.auth = {
          username: localStorage.token,
          password: 'unused'
        }
        this.$axios.get('/api/v1000/elevated/utilization_rate', {params : reqParams}).then(res => {
          let data = res.data
          if (data && data.length > 0) {
            data.forEach((item, index) => {
              let list = item.list
              for (let key in list) {
                let value = list[key];
                if (key === this.specialKey) {
                  let pValue = (value*100).toPrecision(12);
                  pValue = parseFloat(pValue).toFixed(2);
                  value = pValue + '%';
                  list[key] = value
                }
                data[index] = item
              }
            })
            this.utilizationRateList = data
          }
        })
        this.$axios.defaults.auth = {
          username: localStorage.token,
          password: 'unused'
        }
        this.$axios.get('/api/v1000/elevated/storagebin', {params : reqParams}).then(res => {
          let data = res.data
          // console.log("storagebin:" + JSON.stringify(data))
          if (data && data.length > 0) {
            if (this.type === '1') {
              data.forEach((item, index) => {
                let list = item.list;
                list.sort(this.sortBy('name'));
              })
            }
            this.storagebinList = data
          }
        })
        /*let data = [{"name": "\u4e00\u53f7\u8d27\u67b6", "list": [{"name": "01-01-02", "status": "Q"}, {"name": "01-01-03", "status": "Q"}, {"name": "01-01-04", "status": null}, {"name": "01-01-05", "status": ""}, {"name": "01-01-06", "status": null}, {"name": "01-01-07", "status": ""}, {"name": "01-01-08", "status": ""}, {"name": "01-01-09", "status": ""}, {"name": "01-01-10", "status": ""}, {"name": "01-01-11", "status": null}, {"name": "01-01-12", "status": null}, {"name": "01-01-13", "status": null}, {"name": "01-01-14", "status": ""}, {"name": "01-01-15", "status": ""}, {"name": "01-01-16", "status": null}, {"name": "01-01-17", "status": null}, {"name": "01-01-18", "status": null}, {"name": "01-01-19", "status": null}, {"name": "01-01-20", "status": ""}, {"name": "01-01-21", "status": ""}, {"name": "01-01-22", "status": ""}, {"name": "01-01-23", "status": ""}, {"name": "01-01-24", "status": ""}, {"name": "01-01-25", "status": ""}, {"name": "01-01-26", "status": ""}, {"name": "01-01-27", "status": ""}, {"name": "01-01-28", "status": ""}, {"name": "01-01-29", "status": ""}, {"name": "01-01-30", "status": ""}, {"name": "01-01-31", "status": ""}, {"name": "01-01-32", "status": ""}, {"name": "01-02-02", "status": "Q"}, {"name": "01-02-03", "status": "Q"}, {"name": "01-02-04", "status": null}, {"name": "01-02-05", "status": null}, {"name": "01-02-06", "status": null}, {"name": "01-02-07", "status": ""}, {"name": "01-02-08", "status": ""}, {"name": "01-02-09", "status": ""}, {"name": "01-02-10", "status": ""}, {"name": "01-02-11", "status": null}, {"name": "01-02-12", "status": null}, {"name": "01-02-13", "status": null}, {"name": "01-02-14", "status": ""}, {"name": "01-02-15", "status": ""}, {"name": "01-02-16", "status": null}, {"name": "01-02-17", "status": null}, {"name": "01-02-18", "status": null}, {"name": "01-02-19", "status": null}, {"name": "01-02-20", "status": ""}, {"name": "01-02-21", "status": ""}, {"name": "01-02-22", "status": ""}, {"name": "01-02-23", "status": ""}, {"name": "01-02-24", "status": ""}, {"name": "01-02-25", "status": ""}, {"name": "01-02-26", "status": ""}, {"name": "01-02-27", "status": ""}, {"name": "01-02-28", "status": ""}, {"name": "01-02-29", "status": ""}, {"name": "01-02-30", "status": ""}, {"name": "01-02-31", "status": ""}, {"name": "01-02-32", "status": ""}, {"name": "01-03-02", "status": "Q"}, {"name": "01-03-03", "status": "Q"}, {"name": "01-03-04", "status": null}, {"name": "01-03-05", "status": ""}, {"name": "01-03-06", "status": null}, {"name": "01-03-07", "status": ""}, {"name": "01-03-08", "status": ""}, {"name": "01-03-09", "status": ""}, {"name": "01-03-10", "status": ""}, {"name": "01-03-11", "status": null}, {"name": "01-03-12", "status": null}, {"name": "01-03-13", "status": null}, {"name": "01-03-14", "status": null}, {"name": "01-03-15", "status": null}, {"name": "01-03-16", "status": null}, {"name": "01-03-17", "status": null}, {"name": "01-03-18", "status": null}, {"name": "01-03-19", "status": null}, {"name": "01-03-20", "status": ""}, {"name": "01-03-21", "status": ""}, {"name": "01-03-22", "status": null}, {"name": "01-03-23", "status": ""}, {"name": "01-03-24", "status": ""}, {"name": "01-03-25", "status": ""}, {"name": "01-03-26", "status": ""}, {"name": "01-03-27", "status": ""}, {"name": "01-03-28", "status": ""}, {"name": "01-03-29", "status": ""}, {"name": "01-03-30", "status": ""}, {"name": "01-03-31", "status": ""}, {"name": "01-03-32", "status": ""}, {"name": "01-04-02", "status": "Q"}, {"name": "01-04-03", "status": null}, {"name": "01-04-04", "status": null}, {"name": "01-04-05", "status": null}, {"name": "01-04-06", "status": null}, {"name": "01-04-07", "status": null}, {"name": "01-04-08", "status": null}, {"name": "01-04-09", "status": null}, {"name": "01-04-10", "status": null}, {"name": "01-04-11", "status": null}, {"name": "01-04-12", "status": null}, {"name": "01-04-13", "status": null}, {"name": "01-04-14", "status": null}, {"name": "01-04-15", "status": null}, {"name": "01-04-16", "status": null}, {"name": "01-04-17", "status": null}, {"name": "01-04-18", "status": null}, {"name": "01-04-19", "status": null}, {"name": "01-04-20", "status": ""}, {"name": "01-04-21", "status": ""}, {"name": "01-04-22", "status": null}, {"name": "01-04-23", "status": ""}, {"name": "01-04-24", "status": ""}, {"name": "01-04-25", "status": ""}, {"name": "01-04-26", "status": ""}, {"name": "01-04-27", "status": ""}, {"name": "01-04-28", "status": ""}, {"name": "01-04-29", "status": ""}, {"name": "01-04-30", "status": ""}, {"name": "01-04-31", "status": ""}, {"name": "01-04-32", "status": ""}, {"name": "01-05-02", "status": null}, {"name": "01-05-03", "status": null}, {"name": "01-05-04", "status": null}, {"name": "01-05-05", "status": null}, {"name": "01-05-06", "status": null}, {"name": "01-05-07", "status": null}, {"name": "01-05-08", "status": null}, {"name": "01-05-09", "status": null}, {"name": "01-05-10", "status": null}, {"name": "01-05-11", "status": null}, {"name": "01-05-12", "status": null}, {"name": "01-05-13", "status": null}, {"name": "01-05-14", "status": null}, {"name": "01-05-15", "status": null}, {"name": "01-05-16", "status": null}, {"name": "01-05-17", "status": null}, {"name": "01-05-18", "status": null}, {"name": "01-05-19", "status": null}, {"name": "01-05-20", "status": null}, {"name": "01-05-21", "status": null}, {"name": "01-05-22", "status": null}, {"name": "01-05-23", "status": null}, {"name": "01-05-24", "status": null}, {"name": "01-05-25", "status": null}, {"name": "01-05-26", "status": null}, {"name": "01-05-27", "status": null}, {"name": "01-05-28", "status": null}, {"name": "01-05-29", "status": null}, {"name": "01-05-30", "status": null}, {"name": "01-05-31", "status": null}, {"name": "01-05-32", "status": null}, {"name": "01-06-02", "status": null}, {"name": "01-06-03", "status": null}, {"name": "01-06-04", "status": null}, {"name": "01-06-05", "status": null}, {"name": "01-06-06", "status": null}, {"name": "01-06-07", "status": null}, {"name": "01-06-08", "status": null}, {"name": "01-06-09", "status": null}, {"name": "01-06-10", "status": null}, {"name": "01-06-11", "status": null}, {"name": "01-06-12", "status": null}, {"name": "01-06-13", "status": null}, {"name": "01-06-14", "status": null}, {"name": "01-06-15", "status": null}, {"name": "01-06-16", "status": null}, {"name": "01-06-17", "status": null}, {"name": "01-06-18", "status": null}, {"name": "01-06-19", "status": null}, {"name": "01-06-20", "status": null}, {"name": "01-06-21", "status": null}, {"name": "01-06-22", "status": null}, {"name": "01-06-23", "status": null}, {"name": "01-06-24", "status": null}, {"name": "01-06-25", "status": null}, {"name": "01-06-26", "status": null}, {"name": "01-06-27", "status": null}, {"name": "01-06-28", "status": null}, {"name": "01-06-29", "status": null}, {"name": "01-06-30", "status": null}, {"name": "01-06-31", "status": null}, {"name": "01-06-32", "status": null}]}, {"name": "\u4e8c\u53f7\u8d27\u67b6", "list": [{"name": "02-01-02", "status": null}, {"name": "02-01-03", "status": null}, {"name": "02-01-04", "status": null}, {"name": "02-01-05", "status": null}, {"name": "02-01-06", "status": ""}, {"name": "02-01-07", "status": ""}, {"name": "02-01-08", "status": ""}, {"name": "02-01-09", "status": ""}, {"name": "02-01-10", "status": ""}, {"name": "02-01-11", "status": null}, {"name": "02-01-12", "status": ""}, {"name": "02-01-13", "status": ""}, {"name": "02-01-14", "status": ""}, {"name": "02-01-15", "status": ""}, {"name": "02-01-16", "status": ""}, {"name": "02-01-17", "status": ""}, {"name": "02-01-18", "status": ""}, {"name": "02-01-19", "status": ""}, {"name": "02-01-20", "status": ""}, {"name": "02-01-21", "status": ""}, {"name": "02-01-22", "status": "Q"}, {"name": "02-01-23", "status": "Q"}, {"name": "02-01-24", "status": "Q"}, {"name": "02-01-25", "status": "Q"}, {"name": "02-01-26", "status": "Q"}, {"name": "02-01-27", "status": "Q"}, {"name": "02-01-28", "status": "Q"}, {"name": "02-01-29", "status": null}, {"name": "02-01-30", "status": null}, {"name": "02-01-31", "status": null}, {"name": "02-01-32", "status": ""}, {"name": "02-02-02", "status": ""}, {"name": "02-02-03", "status": ""}, {"name": "02-02-04", "status": ""}, {"name": "02-02-05", "status": ""}, {"name": "02-02-06", "status": ""}, {"name": "02-02-07", "status": ""}, {"name": "02-02-08", "status": ""}, {"name": "02-02-09", "status": null}, {"name": "02-02-10", "status": null}, {"name": "02-02-11", "status": ""}, {"name": "02-02-12", "status": ""}, {"name": "02-02-13", "status": ""}, {"name": "02-02-14", "status": ""}, {"name": "02-02-15", "status": ""}, {"name": "02-02-16", "status": ""}, {"name": "02-02-17", "status": ""}, {"name": "02-02-18", "status": ""}, {"name": "02-02-19", "status": ""}, {"name": "02-02-20", "status": ""}, {"name": "02-02-21", "status": ""}, {"name": "02-02-22", "status": ""}, {"name": "02-02-23", "status": ""}, {"name": "02-02-24", "status": ""}, {"name": "02-02-25", "status": ""}, {"name": "02-02-26", "status": ""}, {"name": "02-02-27", "status": ""}, {"name": "02-02-28", "status": ""}, {"name": "02-02-29", "status": ""}, {"name": "02-02-30", "status": null}, {"name": "02-02-31", "status": null}, {"name": "02-02-32", "status": null}, {"name": "02-03-01", "status": null}, {"name": "02-03-02", "status": null}, {"name": "02-03-03", "status": null}, {"name": "02-03-04", "status": null}, {"name": "02-03-05", "status": null}, {"name": "02-03-06", "status": null}, {"name": "02-03-07", "status": null}, {"name": "02-03-08", "status": null}, {"name": "02-03-09", "status": null}, {"name": "02-03-10", "status": null}, {"name": "02-03-11", "status": null}, {"name": "02-03-12", "status": null}, {"name": "02-03-13", "status": ""}, {"name": "02-03-14", "status": ""}, {"name": "02-03-15", "status": ""}, {"name": "02-03-16", "status": ""}, {"name": "02-03-17", "status": ""}, {"name": "02-03-18", "status": ""}, {"name": "02-03-19", "status": null}, {"name": "02-03-20", "status": null}, {"name": "02-03-21", "status": null}, {"name": "02-03-22", "status": null}, {"name": "02-03-23", "status": null}, {"name": "02-03-24", "status": null}, {"name": "02-03-25", "status": null}, {"name": "02-03-26", "status": null}, {"name": "02-03-27", "status": null}, {"name": "02-03-28", "status": null}, {"name": "02-03-29", "status": null}, {"name": "02-03-30", "status": null}, {"name": "02-03-31", "status": null}, {"name": "02-03-32", "status": null}, {"name": "02-04-01", "status": null}, {"name": "02-04-02", "status": null}, {"name": "02-04-03", "status": null}, {"name": "02-04-04", "status": null}, {"name": "02-04-05", "status": null}, {"name": "02-04-06", "status": null}, {"name": "02-04-07", "status": null}, {"name": "02-04-08", "status": null}, {"name": "02-04-09", "status": null}, {"name": "02-04-10", "status": null}, {"name": "02-04-11", "status": null}, {"name": "02-04-12", "status": null}, {"name": "02-04-13", "status": null}, {"name": "02-04-14", "status": null}, {"name": "02-04-15", "status": null}, {"name": "02-04-16", "status": null}, {"name": "02-04-17", "status": null}, {"name": "02-04-18", "status": null}, {"name": "02-04-19", "status": null}, {"name": "02-04-20", "status": null}, {"name": "02-04-21", "status": null}, {"name": "02-04-22", "status": null}, {"name": "02-04-23", "status": null}, {"name": "02-04-24", "status": null}, {"name": "02-04-25", "status": null}, {"name": "02-04-26", "status": null}, {"name": "02-04-27", "status": null}, {"name": "02-04-28", "status": null}, {"name": "02-04-29", "status": null}, {"name": "02-04-30", "status": null}, {"name": "02-04-31", "status": null}, {"name": "02-04-32", "status": null}, {"name": "02-05-01", "status": null}, {"name": "02-05-02", "status": null}, {"name": "02-05-03", "status": null}, {"name": "02-05-04", "status": null}, {"name": "02-05-05", "status": null}, {"name": "02-05-06", "status": null}, {"name": "02-05-07", "status": null}, {"name": "02-05-08", "status": null}, {"name": "02-05-09", "status": null}, {"name": "02-05-10", "status": ""}, {"name": "02-05-11", "status": ""}, {"name": "02-05-12", "status": ""}, {"name": "02-05-13", "status": ""}, {"name": "02-05-14", "status": ""}, {"name": "02-05-15", "status": ""}, {"name": "02-05-16", "status": ""}, {"name": "02-05-17", "status": ""}, {"name": "02-05-18", "status": ""}, {"name": "02-05-19", "status": ""}, {"name": "02-05-20", "status": ""}, {"name": "02-05-21", "status": ""}, {"name": "02-05-22", "status": ""}, {"name": "02-05-23", "status": ""}, {"name": "02-05-24", "status": ""}, {"name": "02-05-25", "status": ""}, {"name": "02-05-26", "status": ""}, {"name": "02-05-27", "status": ""}, {"name": "02-05-28", "status": ""}, {"name": "02-05-29", "status": ""}, {"name": "02-05-30", "status": ""}, {"name": "02-05-31", "status": ""}, {"name": "02-05-32", "status": ""}, {"name": "02-06-02", "status": null}, {"name": "02-06-03", "status": null}, {"name": "02-06-04", "status": null}, {"name": "02-06-05", "status": null}, {"name": "02-06-06", "status": null}, {"name": "02-06-07", "status": null}, {"name": "02-06-08", "status": null}, {"name": "02-06-09", "status": null}, {"name": "02-06-10", "status": null}, {"name": "02-06-11", "status": null}, {"name": "02-06-12", "status": null}, {"name": "02-06-13", "status": null}, {"name": "02-06-14", "status": null}, {"name": "02-06-15", "status": null}, {"name": "02-06-16", "status": null}, {"name": "02-06-17", "status": null}, {"name": "02-06-18", "status": null}, {"name": "02-06-19", "status": null}, {"name": "02-06-20", "status": null}, {"name": "02-06-21", "status": null}, {"name": "02-06-22", "status": "Q"}, {"name": "02-06-23", "status": "Q"}, {"name": "02-06-24", "status": "Q"}, {"name": "02-06-25", "status": "Q"}, {"name": "02-06-26", "status": "Q"}, {"name": "02-06-27", "status": "Q"}, {"name": "02-06-28", "status": "Q"}, {"name": "02-06-29", "status": "Q"}, {"name": "02-06-30", "status": "Q"}, {"name": "02-06-31", "status": "Q"}, {"name": "02-06-32", "status": "Q"}]}, {"name": "\u4e09\u53f7\u8d27\u67b6", "list": [{"name": "03-01-02", "status": ""}, {"name": "03-01-03", "status": ""}, {"name": "03-01-04", "status": null}, {"name": "03-01-05", "status": ""}, {"name": "03-01-06", "status": ""}, {"name": "03-01-07", "status": ""}, {"name": "03-01-08", "status": ""}, {"name": "03-01-09", "status": ""}, {"name": "03-01-10", "status": null}, {"name": "03-01-11", "status": ""}, {"name": "03-01-12", "status": ""}, {"name": "03-01-13", "status": ""}, {"name": "03-01-14", "status": null}, {"name": "03-01-15", "status": null}, {"name": "03-01-16", "status": ""}, {"name": "03-01-17", "status": ""}, {"name": "03-01-18", "status": ""}, {"name": "03-01-19", "status": ""}, {"name": "03-01-20", "status": ""}, {"name": "03-01-21", "status": ""}, {"name": "03-01-22", "status": ""}, {"name": "03-01-23", "status": ""}, {"name": "03-01-24", "status": ""}, {"name": "03-01-25", "status": ""}, {"name": "03-01-26", "status": null}, {"name": "03-01-27", "status": ""}, {"name": "03-01-28", "status": null}, {"name": "03-01-29", "status": "S"}, {"name": "03-01-30", "status": "S"}, {"name": "03-01-31", "status": "S"}, {"name": "03-01-32", "status": "S"}, {"name": "03-02-02", "status": null}, {"name": "03-02-03", "status": null}, {"name": "03-02-04", "status": null}, {"name": "03-02-05", "status": null}, {"name": "03-02-06", "status": null}, {"name": "03-02-07", "status": null}, {"name": "03-02-08", "status": null}, {"name": "03-02-09", "status": null}, {"name": "03-02-10", "status": null}, {"name": "03-02-11", "status": null}, {"name": "03-02-12", "status": null}, {"name": "03-02-13", "status": null}, {"name": "03-02-14", "status": null}, {"name": "03-02-15", "status": null}, {"name": "03-02-16", "status": null}, {"name": "03-02-17", "status": null}, {"name": "03-02-18", "status": null}, {"name": "03-02-19", "status": null}, {"name": "03-02-20", "status": null}, {"name": "03-02-21", "status": null}, {"name": "03-02-22", "status": null}, {"name": "03-02-23", "status": null}, {"name": "03-02-24", "status": null}, {"name": "03-02-25", "status": null}, {"name": "03-02-26", "status": null}, {"name": "03-02-27", "status": null}, {"name": "03-02-28", "status": null}, {"name": "03-02-29", "status": null}, {"name": "03-02-30", "status": null}, {"name": "03-02-31", "status": null}, {"name": "03-02-32", "status": null}, {"name": "03-03-01", "status": null}, {"name": "03-03-02", "status": ""}, {"name": "03-03-03", "status": ""}, {"name": "03-03-04", "status": ""}, {"name": "03-03-05", "status": ""}, {"name": "03-03-06", "status": ""}, {"name": "03-03-07", "status": ""}, {"name": "03-03-08", "status": ""}, {"name": "03-03-09", "status": ""}, {"name": "03-03-10", "status": ""}, {"name": "03-03-11", "status": ""}, {"name": "03-03-12", "status": ""}, {"name": "03-03-13", "status": ""}, {"name": "03-03-14", "status": ""}, {"name": "03-03-15", "status": ""}, {"name": "03-03-16", "status": ""}, {"name": "03-03-17", "status": ""}, {"name": "03-03-18", "status": ""}, {"name": "03-03-19", "status": ""}, {"name": "03-03-20", "status": ""}, {"name": "03-03-21", "status": ""}, {"name": "03-03-22", "status": null}, {"name": "03-03-23", "status": null}, {"name": "03-03-24", "status": null}, {"name": "03-03-25", "status": null}, {"name": "03-03-26", "status": null}, {"name": "03-03-27", "status": null}, {"name": "03-03-28", "status": null}, {"name": "03-03-29", "status": null}, {"name": "03-03-30", "status": null}, {"name": "03-03-31", "status": null}, {"name": "03-03-32", "status": null}, {"name": "03-04-01", "status": null}, {"name": "03-04-02", "status": null}, {"name": "03-04-03", "status": null}, {"name": "03-04-04", "status": null}, {"name": "03-04-05", "status": null}, {"name": "03-04-06", "status": null}, {"name": "03-04-07", "status": null}, {"name": "03-04-08", "status": null}, {"name": "03-04-09", "status": null}, {"name": "03-04-10", "status": null}, {"name": "03-04-11", "status": null}, {"name": "03-04-12", "status": null}, {"name": "03-04-13", "status": null}, {"name": "03-04-14", "status": null}, {"name": "03-04-15", "status": null}, {"name": "03-04-16", "status": null}, {"name": "03-04-17", "status": null}, {"name": "03-04-18", "status": null}, {"name": "03-04-19", "status": null}, {"name": "03-04-20", "status": null}, {"name": "03-04-21", "status": null}, {"name": "03-04-22", "status": null}, {"name": "03-04-23", "status": null}, {"name": "03-04-24", "status": null}, {"name": "03-04-25", "status": null}, {"name": "03-04-26", "status": null}, {"name": "03-04-27", "status": null}, {"name": "03-04-28", "status": null}, {"name": "03-04-29", "status": null}, {"name": "03-04-30", "status": null}, {"name": "03-04-31", "status": null}, {"name": "03-04-32", "status": null}, {"name": "03-05-01", "status": null}, {"name": "03-05-02", "status": null}, {"name": "03-05-03", "status": null}, {"name": "03-05-04", "status": null}, {"name": "03-05-05", "status": null}, {"name": "03-05-06", "status": null}, {"name": "03-05-07", "status": null}, {"name": "03-05-08", "status": null}, {"name": "03-05-09", "status": null}, {"name": "03-05-10", "status": null}, {"name": "03-05-11", "status": null}, {"name": "03-05-12", "status": null}, {"name": "03-05-13", "status": null}, {"name": "03-05-14", "status": null}, {"name": "03-05-15", "status": null}, {"name": "03-05-16", "status": null}, {"name": "03-05-17", "status": null}, {"name": "03-05-18", "status": null}, {"name": "03-05-19", "status": null}, {"name": "03-05-20", "status": null}, {"name": "03-05-21", "status": null}, {"name": "03-05-22", "status": null}, {"name": "03-05-23", "status": null}, {"name": "03-05-24", "status": null}, {"name": "03-05-25", "status": null}, {"name": "03-05-26", "status": null}, {"name": "03-05-27", "status": null}, {"name": "03-05-28", "status": null}, {"name": "03-05-29", "status": null}, {"name": "03-05-30", "status": null}, {"name": "03-05-31", "status": null}, {"name": "03-05-32", "status": null}, {"name": "03-06-02", "status": null}, {"name": "03-06-03", "status": null}, {"name": "03-06-04", "status": null}, {"name": "03-06-05", "status": null}, {"name": "03-06-06", "status": null}, {"name": "03-06-07", "status": null}, {"name": "03-06-08", "status": null}, {"name": "03-06-09", "status": null}, {"name": "03-06-10", "status": null}, {"name": "03-06-11", "status": null}, {"name": "03-06-12", "status": null}, {"name": "03-06-13", "status": null}, {"name": "03-06-14", "status": null}, {"name": "03-06-15", "status": null}, {"name": "03-06-16", "status": null}, {"name": "03-06-17", "status": null}, {"name": "03-06-18", "status": null}, {"name": "03-06-19", "status": null}, {"name": "03-06-20", "status": null}, {"name": "03-06-21", "status": null}, {"name": "03-06-22", "status": null}, {"name": "03-06-23", "status": null}, {"name": "03-06-24", "status": null}, {"name": "03-06-25", "status": null}, {"name": "03-06-26", "status": null}, {"name": "03-06-27", "status": null}, {"name": "03-06-28", "status": null}, {"name": "03-06-29", "status": null}, {"name": "03-06-30", "status": null}, {"name": "03-06-31", "status": null}, {"name": "03-06-32", "status": null}]}, {"name": "\u56db\u53f7\u8d27\u67b6", "list": [{"name": "04-01-02", "status": "S"}, {"name": "04-01-03", "status": "S"}, {"name": "04-01-04", "status": "S"}, {"name": "04-01-05", "status": "S"}, {"name": "04-01-06", "status": "S"}, {"name": "04-01-07", "status": "S"}, {"name": "04-01-08", "status": "S"}, {"name": "04-01-09", "status": null}, {"name": "04-01-10", "status": "S"}, {"name": "04-01-11", "status": "S"}, {"name": "04-01-12", "status": "S"}, {"name": "04-01-13", "status": "S"}, {"name": "04-01-14", "status": "S"}, {"name": "04-01-15", "status": "S"}, {"name": "04-01-16", "status": "S"}, {"name": "04-01-17", "status": "S"}, {"name": "04-01-18", "status": "S"}, {"name": "04-01-19", "status": "S"}, {"name": "04-01-20", "status": "S"}, {"name": "04-01-21", "status": "S"}, {"name": "04-01-22", "status": "S"}, {"name": "04-01-23", "status": "S"}, {"name": "04-01-24", "status": "S"}, {"name": "04-01-25", "status": "S"}, {"name": "04-01-26", "status": "S"}, {"name": "04-01-27", "status": "S"}, {"name": "04-01-28", "status": "S"}, {"name": "04-01-29", "status": "S"}, {"name": "04-01-30", "status": "S"}, {"name": "04-01-31", "status": "S"}, {"name": "04-01-32", "status": "S"}, {"name": "04-02-02", "status": "Q"}, {"name": "04-02-03", "status": "Q"}, {"name": "04-02-04", "status": "Q"}, {"name": "04-02-05", "status": "Q"}, {"name": "04-02-06", "status": "Q"}, {"name": "04-02-07", "status": "Q"}, {"name": "04-02-08", "status": "Q"}, {"name": "04-02-09", "status": "Q"}, {"name": "04-02-10", "status": "Q"}, {"name": "04-02-11", "status": "Q"}, {"name": "04-02-12", "status": "Q"}, {"name": "04-02-13", "status": "Q"}, {"name": "04-02-14", "status": "Q"}, {"name": "04-02-15", "status": "Q"}, {"name": "04-02-16", "status": "Q"}, {"name": "04-02-17", "status": "Q"}, {"name": "04-02-18", "status": "Q"}, {"name": "04-02-19", "status": "Q"}, {"name": "04-02-20", "status": "Q"}, {"name": "04-02-21", "status": "Q"}, {"name": "04-02-22", "status": ""}, {"name": "04-02-23", "status": ""}, {"name": "04-02-24", "status": ""}, {"name": "04-02-25", "status": ""}, {"name": "04-02-26", "status": ""}, {"name": "04-02-27", "status": ""}, {"name": "04-02-28", "status": ""}, {"name": "04-02-29", "status": ""}, {"name": "04-02-30", "status": ""}, {"name": "04-02-31", "status": "S"}, {"name": "04-02-32", "status": "S"}, {"name": "04-03-02", "status": "Q"}, {"name": "04-03-03", "status": "Q"}, {"name": "04-03-04", "status": "Q"}, {"name": "04-03-05", "status": "Q"}, {"name": "04-03-06", "status": "Q"}, {"name": "04-03-07", "status": "Q"}, {"name": "04-03-08", "status": "Q"}, {"name": "04-03-09", "status": "Q"}, {"name": "04-03-10", "status": "Q"}, {"name": "04-03-11", "status": "Q"}, {"name": "04-03-12", "status": "Q"}, {"name": "04-03-13", "status": "Q"}, {"name": "04-03-14", "status": "Q"}, {"name": "04-03-15", "status": "Q"}, {"name": "04-03-16", "status": "Q"}, {"name": "04-03-17", "status": "Q"}, {"name": "04-03-18", "status": "Q"}, {"name": "04-03-19", "status": "Q"}, {"name": "04-03-20", "status": "Q"}, {"name": "04-03-21", "status": "Q"}, {"name": "04-03-22", "status": null}, {"name": "04-03-23", "status": null}, {"name": "04-03-24", "status": null}, {"name": "04-03-25", "status": null}, {"name": "04-03-26", "status": null}, {"name": "04-03-27", "status": null}, {"name": "04-03-28", "status": null}, {"name": "04-03-29", "status": null}, {"name": "04-03-30", "status": null}, {"name": "04-03-31", "status": null}, {"name": "04-03-32", "status": null}, {"name": "04-04-02", "status": "Q"}, {"name": "04-04-03", "status": "Q"}, {"name": "04-04-04", "status": "Q"}, {"name": "04-04-05", "status": "Q"}, {"name": "04-04-06", "status": "Q"}, {"name": "04-04-07", "status": "Q"}, {"name": "04-04-08", "status": "Q"}, {"name": "04-04-09", "status": "Q"}, {"name": "04-04-10", "status": "Q"}, {"name": "04-04-11", "status": "Q"}, {"name": "04-04-12", "status": "Q"}, {"name": "04-04-13", "status": "Q"}, {"name": "04-04-14", "status": "Q"}, {"name": "04-04-15", "status": "Q"}, {"name": "04-04-16", "status": "Q"}, {"name": "04-04-17", "status": "Q"}, {"name": "04-04-18", "status": "Q"}, {"name": "04-04-19", "status": "Q"}, {"name": "04-04-20", "status": "Q"}, {"name": "04-04-21", "status": "Q"}, {"name": "04-04-22", "status": "Q"}, {"name": "04-04-23", "status": "Q"}, {"name": "04-04-24", "status": "Q"}, {"name": "04-04-25", "status": "Q"}, {"name": "04-04-26", "status": "Q"}, {"name": "04-04-27", "status": "Q"}, {"name": "04-04-28", "status": "Q"}, {"name": "04-04-29", "status": "Q"}, {"name": "04-04-30", "status": "Q"}, {"name": "04-04-31", "status": "Q"}, {"name": "04-04-32", "status": "Q"}, {"name": "04-05-02", "status": null}, {"name": "04-05-03", "status": null}, {"name": "04-05-04", "status": null}, {"name": "04-05-05", "status": null}, {"name": "04-05-06", "status": null}, {"name": "04-05-07", "status": null}, {"name": "04-05-08", "status": null}, {"name": "04-05-09", "status": null}, {"name": "04-05-10", "status": null}, {"name": "04-05-11", "status": null}, {"name": "04-05-12", "status": null}, {"name": "04-05-13", "status": null}, {"name": "04-05-14", "status": null}, {"name": "04-05-15", "status": null}, {"name": "04-05-16", "status": null}, {"name": "04-05-17", "status": null}, {"name": "04-05-18", "status": null}, {"name": "04-05-19", "status": null}, {"name": "04-05-20", "status": null}, {"name": "04-05-21", "status": null}, {"name": "04-05-22", "status": "Q"}, {"name": "04-05-23", "status": "Q"}, {"name": "04-05-24", "status": "Q"}, {"name": "04-05-25", "status": "Q"}, {"name": "04-05-26", "status": "Q"}, {"name": "04-05-27", "status": "Q"}, {"name": "04-05-28", "status": "Q"}, {"name": "04-05-29", "status": "Q"}, {"name": "04-05-30", "status": "Q"}, {"name": "04-05-31", "status": "Q"}, {"name": "04-05-32", "status": "Q"}, {"name": "04-06-02", "status": null}, {"name": "04-06-03", "status": null}, {"name": "04-06-04", "status": null}, {"name": "04-06-05", "status": null}, {"name": "04-06-06", "status": null}, {"name": "04-06-07", "status": null}, {"name": "04-06-08", "status": null}, {"name": "04-06-09", "status": null}, {"name": "04-06-10", "status": null}, {"name": "04-06-11", "status": null}, {"name": "04-06-12", "status": null}, {"name": "04-06-13", "status": null}, {"name": "04-06-14", "status": null}, {"name": "04-06-15", "status": null}, {"name": "04-06-16", "status": null}, {"name": "04-06-17", "status": null}, {"name": "04-06-18", "status": null}, {"name": "04-06-19", "status": null}, {"name": "04-06-20", "status": null}, {"name": "04-06-21", "status": null}, {"name": "04-06-22", "status": null}, {"name": "04-06-23", "status": null}, {"name": "04-06-24", "status": null}, {"name": "04-06-25", "status": null}, {"name": "04-06-26", "status": null}, {"name": "04-06-27", "status": null}, {"name": "04-06-28", "status": null}, {"name": "04-06-29", "status": null}, {"name": "04-06-30", "status": null}, {"name": "04-06-31", "status": null}, {"name": "04-06-32", "status": null}]}, {"name": "\u4e94\u53f7\u8d27\u67b6", "list": [{"name": "05-01-02", "status": null}, {"name": "05-01-03", "status": null}, {"name": "05-01-04", "status": null}, {"name": "05-01-05", "status": null}, {"name": "05-01-06", "status": null}, {"name": "05-01-07", "status": null}, {"name": "05-01-08", "status": null}, {"name": "05-01-09", "status": null}, {"name": "05-01-10", "status": null}, {"name": "05-01-11", "status": null}, {"name": "05-01-12", "status": null}, {"name": "05-01-13", "status": null}, {"name": "05-01-14", "status": null}, {"name": "05-01-15", "status": null}, {"name": "05-01-16", "status": null}, {"name": "05-01-17", "status": null}, {"name": "05-01-18", "status": null}, {"name": "05-01-19", "status": null}, {"name": "05-01-20", "status": null}, {"name": "05-01-21", "status": null}, {"name": "05-01-22", "status": null}, {"name": "05-01-23", "status": null}, {"name": "05-01-24", "status": null}, {"name": "05-01-25", "status": null}, {"name": "05-01-26", "status": ""}, {"name": "05-01-27", "status": ""}, {"name": "05-01-28", "status": null}, {"name": "05-01-29", "status": null}, {"name": "05-01-30", "status": "Q"}, {"name": "05-01-31", "status": "Q"}, {"name": "05-01-32", "status": null}, {"name": "05-01-33", "status": null}, {"name": "05-01-34", "status": null}, {"name": "05-02-02", "status": null}, {"name": "05-02-03", "status": null}, {"name": "05-02-04", "status": null}, {"name": "05-02-05", "status": null}, {"name": "05-02-06", "status": null}, {"name": "05-02-07", "status": null}, {"name": "05-02-08", "status": null}, {"name": "05-02-09", "status": null}, {"name": "05-02-10", "status": null}, {"name": "05-02-11", "status": null}, {"name": "05-02-12", "status": null}, {"name": "05-02-13", "status": null}, {"name": "05-02-14", "status": null}, {"name": "05-02-15", "status": null}, {"name": "05-02-16", "status": null}, {"name": "05-02-17", "status": null}, {"name": "05-02-18", "status": null}, {"name": "05-02-19", "status": null}, {"name": "05-02-20", "status": null}, {"name": "05-02-21", "status": null}, {"name": "05-02-22", "status": null}, {"name": "05-02-23", "status": null}, {"name": "05-02-24", "status": null}, {"name": "05-02-25", "status": null}, {"name": "05-02-26", "status": null}, {"name": "05-02-27", "status": null}, {"name": "05-02-28", "status": null}, {"name": "05-02-29", "status": null}, {"name": "05-02-30", "status": null}, {"name": "05-02-31", "status": null}, {"name": "05-02-32", "status": null}, {"name": "05-02-33", "status": null}, {"name": "05-02-34", "status": null}, {"name": "05-03-01", "status": null}, {"name": "05-03-02", "status": "Q"}, {"name": "05-03-03", "status": "Q"}, {"name": "05-03-04", "status": "Q"}, {"name": "05-03-05", "status": "Q"}, {"name": "05-03-06", "status": "Q"}, {"name": "05-03-07", "status": "Q"}, {"name": "05-03-08", "status": "Q"}, {"name": "05-03-09", "status": "Q"}, {"name": "05-03-10", "status": "Q"}, {"name": "05-03-11", "status": "Q"}, {"name": "05-03-12", "status": "Q"}, {"name": "05-03-13", "status": "Q"}, {"name": "05-03-14", "status": "Q"}, {"name": "05-03-15", "status": "Q"}, {"name": "05-03-16", "status": "Q"}, {"name": "05-03-17", "status": "Q"}, {"name": "05-03-18", "status": "Q"}, {"name": "05-03-19", "status": "Q"}, {"name": "05-03-20", "status": "Q"}, {"name": "05-03-21", "status": "Q"}, {"name": "05-03-22", "status": null}, {"name": "05-03-23", "status": null}, {"name": "05-03-24", "status": null}, {"name": "05-03-25", "status": null}, {"name": "05-03-26", "status": null}, {"name": "05-03-27", "status": null}, {"name": "05-03-28", "status": null}, {"name": "05-03-29", "status": null}, {"name": "05-03-30", "status": null}, {"name": "05-03-31", "status": null}, {"name": "05-03-32", "status": null}, {"name": "05-03-33", "status": null}, {"name": "05-03-34", "status": null}, {"name": "05-04-01", "status": null}, {"name": "05-04-02", "status": ""}, {"name": "05-04-03", "status": ""}, {"name": "05-04-04", "status": ""}, {"name": "05-04-05", "status": ""}, {"name": "05-04-06", "status": ""}, {"name": "05-04-07", "status": ""}, {"name": "05-04-08", "status": ""}, {"name": "05-04-09", "status": ""}, {"name": "05-04-10", "status": ""}, {"name": "05-04-11", "status": ""}, {"name": "05-04-12", "status": ""}, {"name": "05-04-13", "status": ""}, {"name": "05-04-14", "status": ""}, {"name": "05-04-15", "status": ""}, {"name": "05-04-16", "status": ""}, {"name": "05-04-17", "status": ""}, {"name": "05-04-18", "status": ""}, {"name": "05-04-19", "status": ""}, {"name": "05-04-20", "status": ""}, {"name": "05-04-21", "status": ""}, {"name": "05-04-22", "status": ""}, {"name": "05-04-23", "status": ""}, {"name": "05-04-24", "status": ""}, {"name": "05-04-25", "status": ""}, {"name": "05-04-26", "status": ""}, {"name": "05-04-27", "status": ""}, {"name": "05-04-28", "status": ""}, {"name": "05-04-29", "status": ""}, {"name": "05-04-30", "status": ""}, {"name": "05-04-31", "status": ""}, {"name": "05-04-32", "status": ""}, {"name": "05-04-33", "status": ""}, {"name": "05-04-34", "status": ""}, {"name": "05-05-01", "status": null}, {"name": "05-05-02", "status": null}, {"name": "05-05-03", "status": null}, {"name": "05-05-04", "status": null}, {"name": "05-05-05", "status": null}, {"name": "05-05-06", "status": null}, {"name": "05-05-07", "status": null}, {"name": "05-05-08", "status": null}, {"name": "05-05-09", "status": null}, {"name": "05-05-10", "status": null}, {"name": "05-05-11", "status": null}, {"name": "05-05-12", "status": null}, {"name": "05-05-13", "status": null}, {"name": "05-05-14", "status": null}, {"name": "05-05-15", "status": null}, {"name": "05-05-16", "status": null}, {"name": "05-05-17", "status": null}, {"name": "05-05-18", "status": null}, {"name": "05-05-19", "status": null}, {"name": "05-05-20", "status": null}, {"name": "05-05-21", "status": null}, {"name": "05-05-22", "status": "Q"}, {"name": "05-05-23", "status": "Q"}, {"name": "05-05-24", "status": "Q"}, {"name": "05-05-25", "status": "Q"}, {"name": "05-05-26", "status": "Q"}, {"name": "05-05-27", "status": "Q"}, {"name": "05-05-28", "status": "Q"}, {"name": "05-05-29", "status": "Q"}, {"name": "05-05-30", "status": "Q"}, {"name": "05-05-31", "status": "Q"}, {"name": "05-05-32", "status": "Q"}, {"name": "05-05-33", "status": "Q"}, {"name": "05-05-34", "status": "Q"}, {"name": "05-06-02", "status": null}, {"name": "05-06-03", "status": null}, {"name": "05-06-04", "status": null}, {"name": "05-06-05", "status": null}, {"name": "05-06-06", "status": null}, {"name": "05-06-07", "status": null}, {"name": "05-06-08", "status": null}, {"name": "05-06-09", "status": null}, {"name": "05-06-10", "status": null}, {"name": "05-06-11", "status": null}, {"name": "05-06-12", "status": null}, {"name": "05-06-13", "status": null}, {"name": "05-06-14", "status": null}, {"name": "05-06-15", "status": null}, {"name": "05-06-16", "status": null}, {"name": "05-06-17", "status": null}, {"name": "05-06-18", "status": null}, {"name": "05-06-19", "status": null}, {"name": "05-06-20", "status": null}, {"name": "05-06-21", "status": null}, {"name": "05-06-22", "status": null}, {"name": "05-06-23", "status": null}, {"name": "05-06-24", "status": null}, {"name": "05-06-25", "status": null}, {"name": "05-06-26", "status": null}, {"name": "05-06-27", "status": null}, {"name": "05-06-28", "status": null}, {"name": "05-06-29", "status": null}, {"name": "05-06-30", "status": null}, {"name": "05-06-31", "status": null}, {"name": "05-06-32", "status": null}, {"name": "05-06-33", "status": null}, {"name": "05-06-34", "status": null}]}, {"name": "\u516d\u53f7\u8d27\u67b6", "list": [{"name": "06-01-02", "status": null}, {"name": "06-01-03", "status": null}, {"name": "06-01-04", "status": null}, {"name": "06-01-05", "status": null}, {"name": "06-01-06", "status": null}, {"name": "06-01-07", "status": null}, {"name": "06-01-08", "status": null}, {"name": "06-01-09", "status": null}, {"name": "06-01-10", "status": null}, {"name": "06-01-11", "status": null}, {"name": "06-01-12", "status": null}, {"name": "06-01-13", "status": null}, {"name": "06-01-14", "status": null}, {"name": "06-01-15", "status": null}, {"name": "06-01-16", "status": null}, {"name": "06-01-17", "status": null}, {"name": "06-01-18", "status": null}, {"name": "06-01-19", "status": null}, {"name": "06-01-20", "status": null}, {"name": "06-01-21", "status": null}, {"name": "06-01-22", "status": null}, {"name": "06-01-23", "status": null}, {"name": "06-01-24", "status": null}, {"name": "06-01-25", "status": null}, {"name": "06-01-26", "status": null}, {"name": "06-01-27", "status": null}, {"name": "06-01-28", "status": null}, {"name": "06-01-29", "status": null}, {"name": "06-01-30", "status": null}, {"name": "06-01-31", "status": null}, {"name": "06-01-32", "status": null}, {"name": "06-01-33", "status": "Q"}, {"name": "06-01-34", "status": null}, {"name": "06-02-02", "status": null}, {"name": "06-02-03", "status": null}, {"name": "06-02-04", "status": null}, {"name": "06-02-05", "status": null}, {"name": "06-02-06", "status": null}, {"name": "06-02-07", "status": null}, {"name": "06-02-08", "status": null}, {"name": "06-02-09", "status": null}, {"name": "06-02-10", "status": null}, {"name": "06-02-11", "status": null}, {"name": "06-02-12", "status": null}, {"name": "06-02-13", "status": null}, {"name": "06-02-14", "status": null}, {"name": "06-02-15", "status": null}, {"name": "06-02-16", "status": null}, {"name": "06-02-17", "status": null}, {"name": "06-02-18", "status": null}, {"name": "06-02-19", "status": null}, {"name": "06-02-20", "status": null}, {"name": "06-02-21", "status": null}, {"name": "06-02-22", "status": null}, {"name": "06-02-23", "status": null}, {"name": "06-02-24", "status": null}, {"name": "06-02-25", "status": null}, {"name": "06-02-26", "status": null}, {"name": "06-02-27", "status": null}, {"name": "06-02-28", "status": null}, {"name": "06-02-29", "status": null}, {"name": "06-02-30", "status": null}, {"name": "06-02-31", "status": null}, {"name": "06-02-32", "status": null}, {"name": "06-02-33", "status": null}, {"name": "06-02-34", "status": null}, {"name": "06-03-02", "status": null}, {"name": "06-03-03", "status": null}, {"name": "06-03-04", "status": null}, {"name": "06-03-05", "status": null}, {"name": "06-03-06", "status": null}, {"name": "06-03-07", "status": null}, {"name": "06-03-08", "status": null}, {"name": "06-03-09", "status": null}, {"name": "06-03-10", "status": null}, {"name": "06-03-11", "status": null}, {"name": "06-03-12", "status": null}, {"name": "06-03-13", "status": null}, {"name": "06-03-14", "status": null}, {"name": "06-03-15", "status": null}, {"name": "06-03-16", "status": null}, {"name": "06-03-17", "status": null}, {"name": "06-03-18", "status": null}, {"name": "06-03-19", "status": null}, {"name": "06-03-20", "status": null}, {"name": "06-03-21", "status": null}, {"name": "06-03-22", "status": "Q"}, {"name": "06-03-23", "status": "Q"}, {"name": "06-03-24", "status": "Q"}, {"name": "06-03-25", "status": "Q"}, {"name": "06-03-26", "status": "Q"}, {"name": "06-03-27", "status": "Q"}, {"name": "06-03-28", "status": "Q"}, {"name": "06-03-29", "status": "Q"}, {"name": "06-03-30", "status": "Q"}, {"name": "06-03-31", "status": "Q"}, {"name": "06-03-32", "status": "Q"}, {"name": "06-03-33", "status": "Q"}, {"name": "06-03-34", "status": "Q"}, {"name": "06-04-02", "status": null}, {"name": "06-04-03", "status": null}, {"name": "06-04-04", "status": null}, {"name": "06-04-05", "status": null}, {"name": "06-04-06", "status": null}, {"name": "06-04-07", "status": null}, {"name": "06-04-08", "status": null}, {"name": "06-04-09", "status": null}, {"name": "06-04-10", "status": null}, {"name": "06-04-11", "status": null}, {"name": "06-04-12", "status": null}, {"name": "06-04-13", "status": null}, {"name": "06-04-14", "status": null}, {"name": "06-04-15", "status": null}, {"name": "06-04-16", "status": null}, {"name": "06-04-17", "status": null}, {"name": "06-04-18", "status": null}, {"name": "06-04-19", "status": null}, {"name": "06-04-20", "status": null}, {"name": "06-04-21", "status": null}, {"name": "06-04-22", "status": null}, {"name": "06-04-23", "status": null}, {"name": "06-04-24", "status": null}, {"name": "06-04-25", "status": null}, {"name": "06-04-26", "status": null}, {"name": "06-04-27", "status": null}, {"name": "06-04-28", "status": null}, {"name": "06-04-29", "status": null}, {"name": "06-04-30", "status": null}, {"name": "06-04-31", "status": null}, {"name": "06-04-32", "status": null}, {"name": "06-04-33", "status": null}, {"name": "06-04-34", "status": null}, {"name": "06-05-02", "status": null}, {"name": "06-05-03", "status": null}, {"name": "06-05-04", "status": null}, {"name": "06-05-05", "status": null}, {"name": "06-05-06", "status": null}, {"name": "06-05-07", "status": null}, {"name": "06-05-08", "status": null}, {"name": "06-05-09", "status": null}, {"name": "06-05-10", "status": null}, {"name": "06-05-11", "status": null}, {"name": "06-05-12", "status": null}, {"name": "06-05-13", "status": null}, {"name": "06-05-14", "status": null}, {"name": "06-05-15", "status": null}, {"name": "06-05-16", "status": null}, {"name": "06-05-17", "status": null}, {"name": "06-05-18", "status": null}, {"name": "06-05-19", "status": null}, {"name": "06-05-20", "status": null}, {"name": "06-05-21", "status": null}, {"name": "06-05-22", "status": null}, {"name": "06-05-23", "status": null}, {"name": "06-05-24", "status": null}, {"name": "06-05-25", "status": null}, {"name": "06-05-26", "status": null}, {"name": "06-05-27", "status": null}, {"name": "06-05-28", "status": null}, {"name": "06-05-29", "status": null}, {"name": "06-05-30", "status": null}, {"name": "06-05-31", "status": null}, {"name": "06-05-32", "status": null}, {"name": "06-05-33", "status": null}, {"name": "06-05-34", "status": null}, {"name": "06-06-02", "status": null}, {"name": "06-06-03", "status": null}, {"name": "06-06-04", "status": null}, {"name": "06-06-05", "status": null}, {"name": "06-06-06", "status": null}, {"name": "06-06-07", "status": null}, {"name": "06-06-08", "status": null}, {"name": "06-06-09", "status": null}, {"name": "06-06-10", "status": null}, {"name": "06-06-11", "status": null}, {"name": "06-06-12", "status": null}, {"name": "06-06-13", "status": null}, {"name": "06-06-14", "status": null}, {"name": "06-06-15", "status": null}, {"name": "06-06-16", "status": null}, {"name": "06-06-17", "status": null}, {"name": "06-06-18", "status": null}, {"name": "06-06-19", "status": null}, {"name": "06-06-20", "status": null}, {"name": "06-06-21", "status": null}, {"name": "06-06-22", "status": null}, {"name": "06-06-23", "status": null}, {"name": "06-06-24", "status": null}, {"name": "06-06-25", "status": null}, {"name": "06-06-26", "status": null}, {"name": "06-06-27", "status": null}, {"name": "06-06-28", "status": null}, {"name": "06-06-29", "status": null}, {"name": "06-06-30", "status": null}, {"name": "06-06-31", "status": null}, {"name": "06-06-32", "status": null}, {"name": "06-06-33", "status": null}, {"name": "06-06-34", "status": null}]}];
        if (data && data.length > 0) {
          if (this.type === '1') {
            data.forEach((item, index) => {
              let list = item.list;
              list.sort(this.sortBy('name'));
            })
          }
          this.storagebinList = data
        }*/
      },
      redirect(binum, status) {
        if (!status || status == '') {
          status = null
        }
        this.$router.push(`/detail/${this.type}/${binum}/${status}/warehouse`)
      },
      btnClass(status) {
        let btnClazz = 'white-btn'
        if (status === 'Q') {
          btnClazz = 'red-btn'
        } else if (status === 'S') {
          btnClazz = 'yellow-btn'
        } else if (status === '') {
          btnClazz = 'green-btn'
        }
        return btnClazz
      },
      sortBy (field) {
        return function(a, b) {
          let value1 = a[field].substring(3, 5);
          let value2 = b[field].substring(3, 5);
          return value2 - value1;
        }
      },
      isShowBr(item, subIndex) {
        let list = item.list
        let currName = list[subIndex].name.substring(0, 5);
        let lastName = list[subIndex > 0 ? subIndex - 1 : 0 ].name.substring(0, 5);
        if (currName !== lastName) {
          return true
        }
        return false
      },
      isShowNullDiv(item, subIndex) {
        let list = item.list

        let curr = list[subIndex].name
        let currName = curr.substring(curr.length - 2)

        let last = list[subIndex > 0 ? subIndex - 1 : 0 ].name
        let lastName = last.substring(last.length - 2)

        let flag = false
        if (currName === '02' && lastName !== '01') {
          flag = true
        }
        return flag
      }
    },
    components: {
      GoBack: GoBack
    },
    created() {
      this.init()
    }
  }
</script>

<style lang="less" scoped>
  .tl {
    text-align: left;
  }
  .special-content-div {
    width: 4000px;
    padding: 30px;
    .storage-col {
      margin-bottom: 30px;
      .storage-left-col {
        width: 130px;
        text-align: right;
        margin-right: 20px;
        font-size: 18px;
        font-weight: 600;
        color: #333333;
      }
      .storage-right-col {
        width: calc(~"100% - 150px");
        .storage-item-btn {
          margin: 0 5px 5px 0;
        }
        .div-null {
          width: 100px;
          margin: 2px;
          display: inline-block;
        }
      }
    }
  }
  .top-div {
    display: flex;
    padding: 30px;
  }
  .content-div {
    /*margin-top: 50px;*/
    /*width: 4000px;*/
    padding: 30px;
    .storagebin-btn {
      width: 100%;
      height: 90px;
      font-size: 30px;
      font-weight: 600;
    }
  }
  .item-row {
    line-height: 40px;
    font-size: 18px;
    padding: 2px 0 2px 0;
    color: #000000;
    div{
      border-radius: 4px;
    }
  }
  .subItem-left-col {
    text-align: right;
    background-color: #d3dce6;
    padding-right: 10px;
  }
  .subItem-right-col {
    padding: 0 5px 0 5px;
    div {
      padding-left: 10px;
    }
  }
  .top-div {
    .el-col-3 {
      width: 13.8%;
      .item-row {
        font-weight: 500;
      }
    }
    .el-col-6 {
      width: 17%;
      padding-left: 50px;
      .item-row {
        font-weight: 800;
      }
    }
    .el-col-9 {
      width: 40%;
    }
    .el-col-15 {
      width: 60%;
    }
  }
  .green {
    background-color: #19ce50;
  }
</style>
