package com.thezouth.kafka201.member;

public enum NotificationChannel {
    NONE(0x00),
    EMAIL(0x01),
    LINE(0x02),
    ALL(0xFF);

    private final int code;

    NotificationChannel(int code) {
        this.code = code;
    }

    public int getCode() {
        return code;
    }
}
