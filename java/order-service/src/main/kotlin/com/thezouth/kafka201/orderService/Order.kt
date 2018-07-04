package com.thezouth.kafka201.orderService

import java.time.Instant
import javax.persistence.*

@Entity
@Table(name = "order_items")
data class OrderItem (
    @Id @GeneratedValue(strategy = GenerationType.IDENTITY)
    val id: Long? = null,
    val productId: String,
    val amount: Int,
    val pricePerUnit: Double,

    @ManyToOne @JoinColumn(name = "order_id", nullable = false)
    val order: Order? = null
) {
    fun totalPrice(): Double = amount * pricePerUnit
}

@Entity
@Table(name = "orders")
data class Order (
    @Id @GeneratedValue(strategy = GenerationType.IDENTITY)
    val id: Long? = null,

    val customerId: Int?,
    val customerName: String,
    val isMember: Boolean,
    val date: Instant,

    @OneToMany(mappedBy = "order", fetch = FetchType.LAZY)
    val items: List<OrderItem>
)