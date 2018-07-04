package com.thezouth.kafka201.member;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.extension.ExtendWith;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.autoconfigure.web.servlet.AutoConfigureMockMvc;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.test.context.junit.jupiter.SpringExtension;
import org.springframework.test.web.servlet.MockMvc;

import static org.springframework.test.web.servlet.request.MockMvcRequestBuilders.get;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.status;

@ExtendWith(SpringExtension.class)
@SpringBootTest
@AutoConfigureMockMvc
public class MemberControllerTest {
    @Autowired
    private MockMvc mvc;

    @Test
    public void getExistingMember() throws Exception{
        mvc.perform(get("/members/1")).andExpect(status().isOk());
    }

    @Test
    public void getNotExistMember() throws Exception{
        mvc.perform(get("/members/notexist")).andExpect(status().isNotFound());
    }

}
