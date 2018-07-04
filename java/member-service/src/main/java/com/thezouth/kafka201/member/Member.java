package com.thezouth.kafka201.member;

public class Member {
    private final String id;

    private String name;
    private String privilege;
    private String email;
    private String lineAccount;
    private NotificationChannel notificationChannel;

    public Member(String id, String name, String privilege, String email,
                  String lineAccount, NotificationChannel notificationChannel) {
        this.id = id;
        this.name = name;
        this.privilege = privilege;
        this.email = email;
        this.lineAccount = lineAccount;
        this.notificationChannel = notificationChannel;
    }

    public String getId() {
        return id;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getPrivilege() {
        return privilege;
    }

    public void setPrivilege(String privilege) {
        this.privilege = privilege;
    }

    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }

    public String getLineAccount() {
        return lineAccount;
    }

    public void setLineAccount(String lineAccount) {
        this.lineAccount = lineAccount;
    }

    public NotificationChannel getNotificationChannel() {
        return notificationChannel;
    }

    public void setNotificationChannel(NotificationChannel notificationChannel) {
        this.notificationChannel = notificationChannel;
    }
}
