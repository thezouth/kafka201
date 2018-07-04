package com.thezouth.kafka201.member;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.Map;
import java.util.Optional;

@RestController
@RequestMapping(path = "/members")
public class MemberController {
    @Autowired
    MemberService memberService;

    @RequestMapping(path = "/{id}/promote", method = RequestMethod.POST)
    public Map<String, String> promote(@PathVariable String id) {
        memberService.promoteMember(id, "gold");
        return Map.of("status", "success99");
    }

    @RequestMapping(path = "/{id}", method = RequestMethod.GET)
    public ResponseEntity<Member> get(@PathVariable String id) {
        return memberService.getMember(id)
                            .map((m) -> new ResponseEntity<>(m, HttpStatus.OK))
                            .orElse(new ResponseEntity<>(HttpStatus.NOT_FOUND));

    }
}
