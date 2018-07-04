package com.thezouth.kafka201.orderService

import org.hamcrest.MatcherAssert.assertThat
import org.hamcrest.Matchers.*
import org.junit.jupiter.api.Test
import org.junit.jupiter.api.extension.ExtendWith
import org.springframework.beans.factory.annotation.Autowired
import org.springframework.boot.test.autoconfigure.orm.jpa.DataJpaTest
import org.springframework.test.context.junit.jupiter.SpringExtension
import java.time.Instant


@ExtendWith(SpringExtension::class)
@DataJpaTest
class OrderRepositoryTest {

    @Autowired
    lateinit var orderRepository: OrderRepository

    @Test
    fun createAndGet() {
        val orderItems = listOf(
                OrderItem(productId = "cocoa", amount = 5, pricePerUnit = 10.2),
                OrderItem(productId = "flour", amount = 2, pricePerUnit = 11.1)
        )

        val order = Order(
                customerId = null, customerName = "Roong",
                isMember = false, date = Instant.now(),
                items = orderItems
        )

        val actual = orderRepository.save(order)

        assertThat(actual.id, notNullValue())
        assertThat(actual.customerId, equalTo(order.customerId))
        assertThat(actual.customerName, equalTo(order.customerName))
        assertThat(actual.isMember, equalTo(order.isMember))
        assertThat(actual.date, equalTo(order.date))

    }
}