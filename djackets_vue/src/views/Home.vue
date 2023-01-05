<template>
  <div class="home">
    <section class="hero is-medium">
      <div class="hero-body">
        <div class="container">
          <img src="../assets/img/home-img.jpeg" alt="bacground" class="hero-image">
          <h1 class="title">
            Welcome to Baeshake
          </h1>
          <h2 class="subtitle">
            The hot KoreanFood
          </h2>
        </div>
      </div>
    </section>

    <div class="columns is-multiline">

      <ProductBox 
        v-for="product in latestProducts"
        v-bind:key="product.id"
        v-bind:product="product" />
    </div>
  </div>
</template>

<script>
import axios from 'axios'

import ProductBox from '@/components/ProductBox'

export default {
  name: 'Home',
  data() {
    return {
      latestProducts: []
    }
  },
  components: {
    ProductBox
  },
  mounted() {
    this.getLatestProducts()

    document.title = 'Home | Baeshake'
  },
  methods: {
    async getLatestProducts() {
      this.$store.commit('setIsLoading', true)

      await axios
        .get('/api/v1/latest-products/')
        .then(response => {
          this.latestProducts = response.data
        })
        .catch(error => {
          console.log(error)
        })

      this.$store.commit('setIsLoading', false)
    }
  }
}
</script>

<style scoped>

.hero-image {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.columns {
  display: flex;
  flex-wrap: wrap;
  margin-right: -0.75rem;
  margin-left: -0.75rem;
}

</style>