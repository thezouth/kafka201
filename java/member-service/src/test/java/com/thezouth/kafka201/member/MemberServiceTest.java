package com.thezouth.kafka201.member;


import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Nested;

import java.util.List;

import static org.hamcrest.MatcherAssert.assertThat;
import static org.hamcrest.Matchers.is;
import static org.hamcrest.core.IsNull.notNullValue;
import static org.junit.jupiter.api.Assertions.assertThrows;

public class MemberServiceTest {
    private MemberService service;

    @BeforeEach
    public void init() {
        this.service = new MemberService(List.of(
                new Member("1", "Roong", "Silver", "pitsanu_s@hotmail.com",
                        null, NotificationChannel.EMAIL)
        ));
    }

    @Test
    public void getFromExistingId() {
        Member member = service.getMember("1").get();
        assertThat(member, is(notNullValue()));
    }

}
